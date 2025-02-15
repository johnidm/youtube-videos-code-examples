"""
Given a singend 32-bit integer return the reversed version

Example: 123 would be 321

The idea here is to use modular division.

Witch is the difference between modular (%) and floor division (//):

- Modular division return the renainder division of two numbers
- Floor division return the largest integer that of result to the division

"""


def reverse(number: int) -> int:
    remainder = number
    reversed = 0

    while remainder != 0:
        reversed = (remainder % 10) + (reversed * 10)
        remainder //= 10

    # if the number is greather than 32-bit number return 0
    return 0 if remainder > 2**32 else reversed


print(f"Reversed number: {reverse(123347)}")


def is_palindrome(number: int) -> bool:
    reversed = reverse(number)
    return number == reversed


print(f"Is Palindrome: {is_palindrome(1221)}")
print(f"Is Palindrome: {is_palindrome(341)}")
