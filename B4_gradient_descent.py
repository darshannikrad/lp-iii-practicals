"""
Practical B4: Gradient Descent for y = (x + 3)^2
Group B: Machine Learning (ML)

Problem Statement:
Implement the Gradient Descent optimization algorithm to find the local (and global)
minimum of the function y = (x + 3)^2, starting from the point x = 2.

Mathematical Foundation:
- Objective Function: y = f(x) = (x + 3)^2
- Derivative (Gradient): dy/dx = f'(x) = 2 * (x + 3)
- Analytical Minimum: At minimum, dy/dx = 0 => 2 * (x + 3) = 0 => x = -3, y = 0.
- Update Rule: x_new = x_old - (learning_rate * gradient)

Key Concepts & Viva Points:
- Why subtract gradient? Gradient points in the direction of steepest increase.
  Subtracting moves downhill towards the minimum.
- Learning Rate (lr): Step size factor.
  - If lr is too small (e.g., 0.001): Convergence is extremely slow.
  - If lr is optimal (e.g., 0.1): Smooth, geometric decay towards minimum.
  - If lr = 1.0: Update factor (1 - 2*lr) = -1; bounces perpetually between 2 and -8.
  - If lr > 1.0: Diverges to infinity.
- Stopping Criteria: Maximum iterations reached, gradient below threshold, or
  abs(new_x - x) < tolerance.

Execution:
  python3 B4_gradient_descent.py
"""

import sys

def basic_gradient_descent():
    print("=" * 60)
    print("Part 1: Basic Gradient Descent (Fixed 100 Iterations)")
    print("=" * 60)

    x = 2.0       # Starting point specified in problem
    lr = 0.1      # Learning rate (step size)
    epochs = 100

    print(f"Initial point: x = {x}, y = {(x + 3)**2:.4f}, lr = {lr}\n")

    for i in range(epochs):
        grad = 2.0 * (x + 3.0)
        x = x - lr * grad
        if (i + 1) in [1, 2, 3, 5, 10, 20, 50, 100]:
            print(f"Iteration {i + 1:3d}: x = {x:8.5f}, y = {(x + 3)**2:10.6f}, grad = {grad:8.5f}")

    print("\nResult after 100 iterations:")
    print(f"  Local minimum at x = {round(x, 4)}")
    print(f"  Minimum value    y = {round((x + 3)**2, 6)}")


def gradient_descent_with_tolerance():
    print("\n" + "=" * 60)
    print("Part 2: Gradient Descent with Early Stopping & Convergence History")
    print("=" * 60)

    x = 2.0
    lr = 0.1
    tolerance = 1e-6
    max_iter = 1000
    history = [x]

    converged_iter = max_iter
    for i in range(max_iter):
        grad = 2.0 * (x + 3.0)
        new_x = x - lr * grad
        if abs(new_x - x) < tolerance:
            converged_iter = i + 1
            x = new_x
            history.append(x)
            break
        x = new_x
        history.append(x)

    print(f"Converged in {converged_iter} iterations (tolerance = {tolerance})")
    print(f"  Calculated Minimum at x = {round(x, 4)}")
    print(f"  Function value        y = {round((x + 3)**2, 6)}")
    return history


def plot_convergence(history):
    try:
        import numpy as np
        import matplotlib.pyplot as plt

        xs = np.linspace(-6, 4, 200)
        ys = (xs + 3)**2

        plt.figure(figsize=(8, 5))
        plt.plot(xs, ys, label="f(x) = (x + 3)^2", color="blue")
        path_y = [(h + 3)**2 for h in history]
        plt.scatter(history, path_y, color="red", zorder=5, label="Descent Steps")
        plt.plot(history, path_y, color="red", linestyle="--", alpha=0.6)
        plt.title("Gradient Descent Optimization Path for y = (x + 3)^2")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axvline(-3, color="green", linestyle=":", label="Global Min at x = -3")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        print("\nDisplaying plot... (close window to finish)")
        plt.show()
    except Exception as e:
        print(f"\nNote: Plotting skipped ({e}). Run in GUI environment to see plot.")


if __name__ == "__main__":
    basic_gradient_descent()
    history = gradient_descent_with_tolerance()
    # If user passed '--plot' or running interactively, show plot if matplotlib is installed
    if "--plot" in sys.argv:
        plot_convergence(history)
