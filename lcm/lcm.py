#!/usr/bin/python
import math
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

if (a < 1 or b < 1):
    print "input should be integers greater than 1"
    exit(0)

def gcdfinder(n, m):
    """Least Common Multiple finder.
       
       Computes Least Common Multiple of two integers greater than 1 using Euclid's 
       Algorithm to find the greatest common divisor. The most efficient way to find
       the least common multiple is to take the product, then divide by the gcd.

       Args:
          positive integer n greater than one
          postive integer m greater than one
       Returns:
          Least Common Multiple among the two integers inputted
    """
    if (n == 1 or m ==  1):
        return 1
    if (n == 0 or m == 0):
        return max(n,m)
    ret = 0
    if (n == m):
        return n
    if (n > m):
        ret = n % m
        return gcdfinder(m, ret)
    else:
        ret = m % n
        return gcdfinder(n, ret)
    return
        

ret = (a*b)/gcdfinder(a, b)

print ret
