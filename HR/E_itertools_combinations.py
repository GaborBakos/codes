'''
itertools.combinations(iterable, r) 
This tool returns the  length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

INPUT: 
A single line containing the string S and integer value k separated by a space.
TASK:
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
'''

from itertools import combinations

S, k = input().split(' ')
k = int(k)
for x in range(1, k+1):
    [print(''.join(el)) for el in combinations(sorted(S), x)]
