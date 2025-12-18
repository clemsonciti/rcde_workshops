import random


def estimate_pi(n_samples: int) -> float:
    if n_samples <= 0:
        raise ValueError("n_samples must be a positive integer")

    inside = 0
    for _ in range(n_samples):
        x = random.random()
        y = random.random()
        if (x * x + y * y) <= 1.0:
            inside += 1

    return 4.0 * (inside / n_samples)

if __name__ == "__main__":
    print(f"π estimate (demo): {estimate_pi(10_000):.6f} (n=10000)")
