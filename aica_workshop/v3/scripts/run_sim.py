#!/usr/bin/env python3

import argparse
import math
import pathlib
import sys
import time

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from mc_sim.simulate import estimate_pi


RELIABLE_STD_ERROR = 0.01


def warn_low_sample_size(n_samples: int, threshold: float = RELIABLE_STD_ERROR) -> None:
    """Warn if the expected Monte Carlo error exceeds `threshold`."""
    if n_samples <= 0:
        return
    quarter_prob = math.pi / 4
    std_error = 4 * math.sqrt(quarter_prob * (1 - quarter_prob) / n_samples)
    if std_error <= threshold:
        return

    min_samples = math.ceil(
        (16 * quarter_prob * (1 - quarter_prob)) / (threshold**2)
    )
    print(
        (
            f"WARNING: {n_samples} samples give an expected standard error of "
            f"{std_error:.3f}, which is above the {threshold:.3f} threshold. "
            f"Consider using at least {min_samples} samples."
        ),
        file=sys.stderr,
    )

def main() -> int:
    parser = argparse.ArgumentParser(description="Run Monte Carlo π estimation.")
    parser.add_argument(
        "--n-samples",
        type=int,
        default=100_000,
        help="Number of random samples (default: 100000).",
    )
    parser.add_argument(
        "--no-vectorized",
        action="store_true",
        help="Disable NumPy vectorization when counting points.",
    )
    parser.add_argument(
        "--num-workers",
        type=int,
        default=1,
        help="Number of worker processes to use (default: 1).",
    )
    args = parser.parse_args()

    if args.num_workers < 1:
        parser.error("--num-workers must be a positive integer")

    warn_low_sample_size(args.n_samples)

    start = time.perf_counter()
    use_vectorized = not args.no_vectorized
    pi_est = estimate_pi(
        args.n_samples,
        use_vectorized=use_vectorized,
        num_workers=args.num_workers,
    )
    elapsed = time.perf_counter() - start
    worker_info = (
        f", workers={args.num_workers}" if args.num_workers > 1 else ""
    )

    print(
        (
            f"π estimate: {pi_est:.6f} (n={args.n_samples}, "
            f"mode={'vectorized' if use_vectorized else 'sequential'}{worker_info}); "
            f"elapsed: {elapsed:.3f}s"
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
