"""
function fib returns the Fibonocci number.
"""

def fib(n):
    if n is 0:
        return 0
    elif n is 1:
        return 1
    i = 0
    result = [0]
    a = 0 
    b = 1
    while i < n:
        result.append(b)
        a= b
        b= a+b
        i = i + 1
    return result[-1]