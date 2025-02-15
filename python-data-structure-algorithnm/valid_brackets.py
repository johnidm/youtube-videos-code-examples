# Valid brackets problem
# Given a string s containing just the caracters {, }, [, ], (, and )
# determinate if the input strings is valid.

s = ["{", "}", "[", "]"]

h = {
    "{": "}",
    "[": "]",
    "(": ")",
}


def valid_brackets(s):
    if len(s) % 2 != 0:
        return False  # non-pairs items

    for i in range(0, len(s), 2):
        left, right = s[i], s[i + 1]

        if left not in h:
            return False  # don't find the open bracket

        if not h[left] == right:
            return False

    return True


items = [s, ["{"], ["&", "&"], ["(", "}"]]

for item in items:
    print(item, " ", valid_brackets(item))
