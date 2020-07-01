from operator import add, sub
import math

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13.0
    >>> two_of_three(5, 3, 1)
    34.0
    >>> two_of_three(10, 2, 8)
    164.0
    >>> two_of_three(5, 5, 5)
    50.0
    """
    return math.pow(max(a,b),2)+math.pow(max(b,c),2)

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    k=1
    while k<n:
        if n%k==0:
            facator=k
            k+=1
        else:
            k+=1
    return facator
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return 2

def t():
    return 3

def f():
    return 1

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5.0
    16.0
    8.0
    4.0
    2.0
    1.0
    >>> a
    7
    """
    k=1
    print(n)
    while n!=1:
        if n%2==0:
            n/=2
            k+=1
            print(n)
        else:
            n=n*3+1
            k += 1
            print(n)
    return k

