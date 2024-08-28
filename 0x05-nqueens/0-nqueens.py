#!/usr/bin/python3
""" N queens """

def get_n_from_user():
    """ Get N from user input """
    try:
        n = int(input("Enter the value of N: "))
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    return n

def queens(n, i=0, a=[], b=[], c=[]):
    """ Find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

def solve(n):
    """ Solve the N queens problem """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0

if __name__ == "__main__":
    n = get_n_from_user()
    solve(n)
