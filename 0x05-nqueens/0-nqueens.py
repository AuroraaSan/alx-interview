#!/usr/bin/python3
""" N queens """
import sys


#checking for input from user
if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)
#check if N is number
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)
#make sure that N is greater than 4
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
#retrieve N from user 
n = int(sys.argv[1])

def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a