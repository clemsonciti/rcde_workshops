#!/usr/bin/env python3

import argparse
import os
import pathlib
import statistics
import sys
import time
import warnings

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from mc_sim.simulate import estimate_pi


def available_workers() -> int:
    slurm_cpus = os.getenv("SLURM_CPUS_PER_TASK")
    if slurm_cpus and slurm_cpus.isdigit():
        return max(1, int(slurm_cpus))
    return max(1, os.cpu_count() or 1)


def time_estimate(n_samples: int, *, workers: int, vectorized: bool) -> float:
    start = time.perf_counter()
    estimate_pi(n_samples, workers=workers, vectorized=vectorized)
    return time.perf_counter() - start


def format_seconds(value: float) -> str:
    return f"{value:.4f}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Benchmark Monte Carlo π estimation performance."
    )
    parser.add_argument(
        "--n-samples",
        type=int,
        default=5_000_000,
        help="Number of random samples (default: 5000000).",
    )
    parser.add_argument(
        "--repeats",
        type=int,
        default=10,
        help="Number of repeats per setting (default: 10).",
    )
    parser.add_argument(
        "--output-dir",
        type=pathlib.Path,
        default=pathlib.Path("results/sim_bench"),
        help="Directory for plots and markdown output.",
    )
    args = parser.parse_args()

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    workers_max = available_workers()
    worker_modes = [1]
    if workers_max > 1:
        worker_modes.append(workers_max)

    summary_rows = []
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for vectorized in (True, False):
            for workers in worker_modes:
                timings = [
                    time_estimate(
                        args.n_samples,
                        workers=workers,
                        vectorized=vectorized,
                    )
                    for _ in range(args.repeats)
                ]
                mean_val = statistics.mean(timings)
                std_val = (
                    statistics.stdev(timings)
                    if len(timings) > 1
                    else 0.0
                )
                summary_rows.append(
                    {
                        "mode": "vectorized" if vectorized else "non-vectorized",
                        "workers": workers,
                        "mean": mean_val,
                        "std": std_val,
                    }
                )

    worker_timings = []
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for workers in range(1, workers_max + 1):
            elapsed = time_estimate(
                args.n_samples,
                workers=workers,
                vectorized=True,
            )
            worker_timings.append((workers, elapsed))

    plot_path = output_dir / "vectorized_workers.png"
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(7, 4))
        plt.plot(
            [item[0] for item in worker_timings],
            [item[1] for item in worker_timings],
            marker="o",
            color="#1f77b4",
        )
        plt.title("Vectorized runtime by worker count")
        plt.xlabel("Workers")
        plt.ylabel("Elapsed time (s)")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(plot_path, dpi=150)
        plt.close()
    except ImportError as exc:
        raise SystemExit(
            "matplotlib is required to generate the plot. "
            "Install it or run on a node with matplotlib available."
        ) from exc

    report_path = output_dir / "benchmark_report.md"
    table_lines = [
        "| Mode | Workers | Mean Time (s) | Std Time (s) |",
        "| --- | --- | --- | --- |",
    ]
    for row in summary_rows:
        table_lines.append(
            f"| {row['mode']} | {row['workers']} | "
            f"{format_seconds(row['mean'])} | {format_seconds(row['std'])} |"
        )

    report = "\n".join(
        [
            "# Monte Carlo π timing results",
            "",
            (
                "This report summarizes runtime measurements for the Monte Carlo π "
                "simulation. The first section compares vectorized vs non-vectorized "
                "implementations on a single core and on all available cores, running "
                f"each setting {args.repeats} times with {args.n_samples} samples. "
                "The second section shows how runtime scales with worker count for "
                "the vectorized implementation (single run per worker count)."
            ),
            "",
            "## Timing across settings",
            "",
            "\n".join(table_lines),
            "",
            "## Vectorized scaling by workers",
            "",
            "![Vectorized runtime by worker count](vectorized_workers.png)",
        ]
    )

    report_path.write_text(report, encoding="utf-8")

    print(f"Wrote report to {report_path}")
    print(f"Wrote plot to {plot_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
