'''
Task

You are given a string S. 
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string  and the integer value .
'''


from itertools import permutations

string, N = input().split(' ')
x = sorted(permutations(string, int(N)))
for perm in x:
    print(''.join(perm))
