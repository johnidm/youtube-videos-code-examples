"""
Testing Your Code with Examples!

Doctest is a built-in Python module that allows you to write tests for your code

Steps for running doctest:
    - Write your function with the examples in the docstring.
    - Use Python's command to run doctest on your file.

Run Doctests:
    Automaticaly:
        if __name__ == "__main__":
            import doctest
            doctest.testmod()
    Manually:
        python -m doctest -v main.py

Tips for writing doctests:
    - Write your tests in the docstring.
    - Use ellipses (...) to shorten traceback messages in expected outputs.
    - Don't forget to run doctests regularly! If your code changes, your tests should too.

Key Benefits of Using Doctest
    - Ensures examples in documentation stay correct
    - No separate test files needed
    - Quick and lightweight testing for small functions
"""


def add(a: int, b: int) -> int:
    """
    Adds two numbers together.

    Args:
        a (int): The first number to add.
        b (int): The second number to add.
    Returns:
        int: The sum of a and b.
    Examples:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b


def factorial(n: int) -> int:
    """
    Returns the factorial of a number.
    Args:
        n (int): A non-negative integer to calculate the factorial of.
    Returns:
        int: The factorial of n (n!).
    Examples:
    >>> factorial(5)
    120
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    return 1 if n == 0 else n * factorial(n - 1)


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
