#!/usr/bin/env python3

import argparse
import pathlib
import sys
import time

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
    args = parser.parse_args()

    start = time.perf_counter()
    pi_est = estimate_pi(args.n_samples)
    elapsed = time.perf_counter() - start

    print(f"π estimate: {pi_est:.6f} (n={args.n_samples}); elapsed: {elapsed:.3f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
