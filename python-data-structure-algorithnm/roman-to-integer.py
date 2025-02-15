"""
Given a roman numeral string s convert it ro an integer.
"""


def to_integer(s: str) -> int:
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    current = 0
    previous = 0
    result = 0

    for n in range(len(s) - 1, -1, -1):
        current = roman[s[n]]

        if current < previous:
            result -= current
        else:
            result += current

        previous = current

    return result


romans = [
    ("III", 3),
    ("XLIX", 49),
    ("MMM", 3000),
    ("LVII", 57),
]

for s, r in romans:
    rr = to_integer(s)
    print(f"R: {s}", rr)
    assert rr == r
    print("-------")
