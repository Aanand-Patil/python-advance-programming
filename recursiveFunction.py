# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# factorial(5)

# using iterative function
# def iterative_factorial(n):
#     result = 1
#     for i in range(2,n+1):
#         result *= i
#     return result

# iterative_factorial(1)


# fibonaci series recursive
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# b=fib(5)    
# print(b)

# fibonaci series iteratively
# def fibi(n):
#     old, new = 0, 1
#     if n == 0:
#         return 0
#     for i in range(n-1):
#         old, new = new, old + new
#     return new

# fibi(4)

# from timeit import Timer

# t1 = Timer("fib(10)","from fibonacci import fib")

# for i in range(1, 20):
#     cmd = "fib(" + str(i) + ")"
#     t1 = Timer(cmd, "from fibonacci import fib")
#     time1 = t1.timeit(3)
#     cmd = "fibi(" + str(i) + ")"
#     t2 = Timer(cmd, "from fibonacci import fibi")
#     time2 = t2.timeit(3)
#     print(f"n={i:2d}, fib: {time1:8.6f}, fibi:  {time2:7.6f}, time1/time2: {time1/time2:10.2f}")

# Think of a recursive version of the function f(n) = 3 * n, i.e. the multiples of 3

# def mult3(n):
#     if n == 1:
#         return 3
#     else:
#         return mult3(n-1) + 3

# for i in range(1,10):
#         print(mult3(i))

# Write a recursive Python function that returns the sum of the first n integers. (Hint: The function will be similiar to the factorial function!)

# def sum_n(n):
#     if n== 0:
#         return 0
#     else:
#         return n + sum_n(n-1)

# Exercise 3
# Write a function which implements the Pascal's triangle:

# def pascal(n):
#     if n == 1:
#         return [1]
#     else:
#         p_line = pascal(n-1)
#         line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
#         line.insert(0,1)
#         line.append(1)
#     return line

# print(pascal(4))

# prime numbers in recursively sorted
from math import sqrt

def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = [j for i in p for j in range(i*2, n + 1, i)]
        p = [x for x in range(2, n + 1) if x not in no_p]
        return p


print(primes(100))






















