def bisection_roots(x: float, n: float, epsilon: float = 1e-7, max_iterations: int = 100):
    """Finds the nth root of a positive number using the bisection method.

    Args:
    x: The number to find the root of.
    n: The root to calculate.
    epsilon: The desired accuracy of the result.
    max_iterations: The maximum number of iterations.

    Returns:
    An approximation of the nth root of x.

    Raises:
    ValueError: If x is negative or n is less than or equal to zero.
    """

    if x < 0 or n <= 0:
        raise ValueError("x must be positive and n must be greater than zero")

    f = lambda y: y**n - x
    low = 0
    high = x if x > 1 else 1
    mid = 0

    for _ in range(max_iterations):
        mid = (low + high) / 2
        if abs(f(mid)) < epsilon:
            return mid
        elif f(mid) < 0:
            low = mid
        else:
            high = mid

    return mid
