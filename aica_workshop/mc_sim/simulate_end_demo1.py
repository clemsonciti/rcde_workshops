"""Monte Carlo helpers for estimating π."""

from typing import Any

import numpy as np


PointArray = Any  # NumPy typing requires optional dependencies; keep it generic for simplicity.


def random_unit_points(n_samples: int) -> PointArray:
    """Return `n_samples` points sampled uniformly inside [0, 1]^2."""

    rng = np.random.default_rng()
    return rng.random((n_samples, 2))


def count_inside_points(points: PointArray) -> int:
    """Return how many of the provided points lie inside the quarter circle."""

    distances_squared = np.sum(points * points, axis=1)
    return int(np.count_nonzero(distances_squared <= 1.0))


def estimate_pi(n_samples: int) -> float:
    """Return a Monte Carlo estimate of π using `n_samples` random points."""

    if n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")

    points = random_unit_points(n_samples)
    inside = count_inside_points(points)
    return 4 * inside / n_samples

if __name__ == "__main__":
    print(f"π estimate (demo): {estimate_pi(10_000):.6f} (n=10000)")
