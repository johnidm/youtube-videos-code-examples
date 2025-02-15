# Longest Common Prefix
# Given an array of strings str, find the longest common
# prefix string amongst all items

s = ["flower", "flow", "flight"]


def find_shortest(s: list[str]) -> str:
    n = min(s, key=len)

    for i in range(len(n)):
        for item in s:
            if n[i] != item[i]:
                return n[:i]

    return ""


print(find_shortest(s))
