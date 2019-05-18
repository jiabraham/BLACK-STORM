#!/usr/bin/python
import math
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

if (a < 1 or b < 1):
    print "input should be integers greater than 1"
    exit(0)

def euclid(n, m):
    if (n == 1 or m ==  1):
        return 1
    if (n == 0 or m == 0):
        return max(n,m)
    ret = 0
    if (n == m):
        return n
    if (n > m):
        ret = n % m
        return euclid(m, ret)
    else:
        ret = m % n
        return euclid(n, ret)
    return

ret = euclid(a, b)

print ret
