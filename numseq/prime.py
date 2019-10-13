""" 
- primes(n) returns a list of all primes less than n
- is_prime(m) returns a boolean indicating whether m is a prime number
"""
def is_prime(num):
    if num > 1:
        for index in range(2,num):
            if (num % index) == 0:
                return False
        else:
            return True
    else:
        return False


def primes(n):
    return [num for num in range(2, n) if is_prime(num)]