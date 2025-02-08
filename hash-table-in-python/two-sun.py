# Given an array of integer numbers, find the index  of the two numbers that sum to a specific target.

numbers = [1, 2, 4, 8]
target = 9


def is_two_sun(numbers: list[int], target: int) -> bool:
    h = {}

    for n in range(0, len(numbers)):
        complement = target - numbers[n]

        if complement in h:
            return h[complement], n

        h[numbers[n]] = n

    return False


print(f"Is two sun: {(is_two_sun(numbers, target))}")

