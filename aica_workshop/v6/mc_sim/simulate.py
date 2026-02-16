"""Monte Carlo helpers for estimating π."""

from functools import partial
from typing import Any

import concurrent.futures
import numpy as np
import warnings

PointArray = Any  # NumPy typing requires optional dependencies; keep it generic for simplicity.

MIN_ROBUST_SAMPLES = 10_000


def random_unit_points(n_samples: int) -> PointArray:
    """Return `n_samples` points sampled uniformly inside [0, 1]^2."""

    rng = np.random.default_rng()
    return rng.random((n_samples, 2))


def count_inside_points(points: PointArray) -> int:
    """Return how many of the provided points lie inside the quarter circle."""

    distances_squared = np.sum(points * points, axis=1)
    return int(np.count_nonzero(distances_squared <= 1.0))


def _count_inside_chunk(n_samples: int, *, vectorized: bool = True) -> int:
    """Return how many random points fall inside the quarter circle for one chunk."""

    rng = np.random.default_rng()
    if vectorized:
        points = random_unit_points(n_samples)
        return count_inside_points(points)

    inside = 0
    for _ in range(n_samples):
        x, y = rng.random(2)
        inside += int(x * x + y * y <= 1.0)
    return inside


def estimate_pi(n_samples: int, *, workers: int = 1, vectorized: bool = True) -> float:
    """Return a Monte Carlo estimate of π using `n_samples` random points."""

    if n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")
    if workers <= 0:
        raise ValueError("workers must be a positive integer")

    if n_samples < MIN_ROBUST_SAMPLES:
        warnings.warn(
            f"{n_samples} samples may be too low for a robust π estimate; "
            f"consider using at least {MIN_ROBUST_SAMPLES} samples.",
            stacklevel=2,
        )

    actual_workers = min(workers, n_samples)
    if actual_workers == 1:
        inside = _count_inside_chunk(n_samples, vectorized=vectorized)
    else:
        base, remainder = divmod(n_samples, actual_workers)
        chunk_sizes = [
            base + (1 if idx < remainder else 0) for idx in range(actual_workers)
        ]
        chunk_worker = partial(_count_inside_chunk, vectorized=vectorized)
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=actual_workers
        ) as executor:
            inside_counts = list(executor.map(chunk_worker, chunk_sizes))
        inside = sum(inside_counts)

    return 4 * inside / n_samples


if __name__ == "__main__":
    print(f"π estimate (demo): {estimate_pi(10_000):.6f} (n=10000)")
