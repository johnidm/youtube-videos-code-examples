"""
Reverse string - recursive approach
"""

def reverse(s: list[str], left: int, right: int):
    if left >= right:
        return 
    
    s[left], s[right] = s[right], s[left]
    reverse(s, left + 1, right - 1)


l = ["h", "e", "l", "l", "o"]

reverse(l, 0, 4)

print(l)
