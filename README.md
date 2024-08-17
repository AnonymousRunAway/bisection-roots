# Bisection Method for Root Finding

This Python script implements the bisection method to find the nth root of a positive number.

# Function:

```python
bisection_roots(x, n, epsilon=1e-7, max_iterations=100):
```
Finds the nth root of a positive number x using the bisection method.
epsilon controls the desired accuracy.
max_iterations sets the maximum number of iterations.

# Sample Usage

```python
import bisection_roots

result = bisection_roots.bisection_roots(8, 3)
print(result)  # Output: approximately 2.0
```
