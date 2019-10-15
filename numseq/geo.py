"""
3 functions, square, triangle, cube. 
"""


def square(n):
    return n**2


def triangle(n):
    result = 0
    while n:
        result = result + n
        n = n - 1
    return result


def cube(n):
    return n**3
