"""
Given an integer n, return a string array answer (1-indexed) where:
- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.
"""

def fizz_buzz(n: int) -> list[str]:
    
    l = []

    for i in range(1, n + 1):
        s = "" # default value
        
        if i % 3 == 0: 
            s += "Fizz" 
        if i % 5 == 0:
            s += "Buzz"
        
        if not s:
            s = str(i)
        
        l.append(s)

    return l

print(fizz_buzz(15))
