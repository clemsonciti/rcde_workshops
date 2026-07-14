#!/usr/bin/env python3

import argparse
import pathlib
import sys
import time
import warnings

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from mc_sim.simulate import estimate_pi


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
        "--num_workers",
        type=int,
        default=1,
        help="Number of worker processes (default: 1).",
    )
    args = parser.parse_args()

    if args.n_samples < 10_000:
        warnings.warn(
            "n-samples is low; the π estimate may be noisy. "
            "Use at least 10000 samples for a more stable estimate.",
            UserWarning,
        )

    start = time.perf_counter()
    use_vectorized = not args.no_vectorized
    pi_est = estimate_pi(
        args.n_samples,
        use_vectorized=use_vectorized,
        num_workers=args.num_workers,
    )
    elapsed = time.perf_counter() - start

    print(
        (
            f"π estimate: {pi_est:.6f} (n={args.n_samples}, "
            f"mode={'vectorized' if use_vectorized else 'sequential'}); "
            f"elapsed: {elapsed:.3f}s"
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
