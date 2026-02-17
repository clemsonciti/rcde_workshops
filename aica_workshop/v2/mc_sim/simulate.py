"""Monte Carlo utilities for estimating π."""

import random
import numpy as np


def random_point() -> tuple[float, float]:
    """Return a random coordinate inside the unit square [0, 1) × [0, 1)."""
    return random.random(), random.random()


def is_inside_unit_circle(x: float, y: float) -> bool:
    """Check whether a point lies within the quarter circle of radius 1."""
    return (x * x + y * y) <= 1.0


def count_points_inside_loop(n_samples: int) -> int:
    """Sample `n_samples` points in pure Python and count hits in the quarter circle."""
    inside = 0
    for _ in range(n_samples):
        x, y = random_point()
        # Count hits that satisfy x^2 + y^2 <= 1.
        if is_inside_unit_circle(x, y):
            inside += 1
    return inside


def count_points_inside_vectorized(n_samples: int) -> int:
    """Sample `n_samples` points with NumPy and count hits in the quarter circle."""
    coords = np.random.random((n_samples, 2))
    inside_mask = np.sum(coords * coords, axis=1) <= 1.0
    # `np.count_nonzero` returns a numpy scalar that we cast to int for consistency.
    return int(np.count_nonzero(inside_mask))


def estimate_pi(n_samples: int, use_vectorized: bool = True) -> float:
    """Estimate π using random sampling inside the unit square.

    The method relies on the fact that the area of a quarter circle with radius 1
    is π/4, so the ratio of points inside the circle to the total samples
    (multiplied by 4) approximates π.
    """
    if n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")

    inside = (
        count_points_inside_vectorized(n_samples)
        if use_vectorized
        else count_points_inside_loop(n_samples)
    )
    # Multiply the ratio by 4 to expand the quarter-circle area back up to π.
    return 4 * inside / n_samples


if __name__ == "__main__":
    print(f"π estimate (demo): {estimate_pi(10_000):.6f} (n=10000)")
