from numseq.prime import primes, is_prime
from numseq.geo import square, triangle, cube
from numseq.fib import fib


def fib_test():
    print("Fibonacci")
    for i in range(10):
        print("{}: {}".format(i, fib(i)))
    print(" ")


def geo_test():
    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))
    print(" ")


def prime_test():
    print("Primes")
    prime_list = primes(1000)
    for p in prime_list[-10:]:
        print(p)
    print("Is 999981 prime? {}".format(is_prime(999981)))
    print("Is 999983 prime? {}".format(is_prime(999983)))


def main():
    fib_test()
    geo_test()
    prime_test()


if __name__ == '__main__':
    print('file being executed directly')
    main()
else:
    print('file being imported')
