"""
What is Memoization?

Memoization is an optimization technique used to improve the performance of functions
by storing the results of expensive function calls and reusing them when the same inputs occur again.

It is particularly useful in scenarios where a function is repeatedly called with the same arguments,
such as recursive algorithms like Fibonacci sequence calculations.

When to Use Memoization
- Recursive functions (e.g., Fibonacci, factorials).
- Dynamic programming problems (e.g., knapsack problem).
- Expensive functions with predictable inputs.
- Caching database or API results for repeated queries.

When Not to Use Memoization
- For functions with highly varied inputs.
- When memory usage is a critical constraint.
- In scenarios where input values are mutable or not hashable.
- Memoization is a powerful technique, but its utility depends on the specific problem and constraints.

"""

from functools import lru_cache
from time import sleep


# Using a Custom Cache Dictionary
# Fibonacci with custom memoization
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]


print(fibonacci(10))  # Output: 55


# Using functools.lru_cache
@lru_cache(maxsize=None)  # Cache unlimited results
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


print(fibonacci_lru(10))  # Output: 55

# Memoizing Expensive Computations
# Simulating an expensive computation


@lru_cache(maxsize=3)  # Limit cache size to 3 results
def expensive_computation(x):
    sleep(2)  # Simulate a time-consuming operation
    return x * x


print(expensive_computation(4))  # Takes 2 seconds
print(expensive_computation(4))  # Instantaneous (cached)
