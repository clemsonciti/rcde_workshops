"""
Monte Carlo π estimator (pure Python, stdlib only).
"""

import random


def estimate_pi(n_samples: int) -> float:
    """
    Estimate π via Monte Carlo sampling.

    Randomly sample points (x, y) uniformly in the unit square [0, 1) × [0, 1)
    and estimate the area of the quarter circle x^2 + y^2 <= 1.

    Args:
        n_samples: Number of random samples to draw. Must be positive.

    Returns:
        Estimated value of π.
    """
    if n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")

    inside = 0
    for _ in range(n_samples):
        x = random.random()
        y = random.random()
        if (x * x + y * y) <= 1.0:
            inside += 1

    return 4.0 * (inside / n_samples)


# TODO(failure-mode): env misconfig (e.g., wrong Python, missing module path, bad venv)
# TODO(failure-mode): resource overuse (e.g., huge n_samples, runaway runtime on login node)
# TODO(failure-mode): logic tweak (e.g., biased RNG usage, wrong domain, incorrect scaling)


if __name__ == "__main__":
    # Seed here (if desired) to make demo runs reproducible.
    # random.seed(0)
    print(f"π estimate (demo): {estimate_pi(10_000):.6f} (n=10000)")
