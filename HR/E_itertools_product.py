'''
    This tool computes the cartesian product of input iterables. 
    It is equivalent to nested for-loops. 
    For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
'''


from itertools import product

A = input()
B = input()

A = [int(el) for el in A.split(' ')]
B = [int(el) for el in B.split(' ')]

[print(x, end=' ') for x in product(A, B)]
print()
