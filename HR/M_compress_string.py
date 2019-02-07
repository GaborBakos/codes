'''
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out https://docs.python.org/2/library/itertools.html#itertools.groupby.

You are given a string S . Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c)  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string S.

Output Format

A single line of output consisting of the modified string.

EXAMPLE:
    1222311

EXPECTED OUTPUT:
    (1, 1) (3, 2) (1, 3) (2, 1)
'''

from itertools import groupby

# [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
# [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
# print([k for k, g in groupby('1222311')]) --> ['1', '2', '3', '1']
# print([list(g) for k, g in groupby('1222311')]) -- [['1'], ['2', '2', '2'], ['3'], ['1', '1']]
# print([(len(list(g)), int(k)) for k, g in groupby('1222311')]) --> [(1, 1), (3, 2), (1, 3), (2, 1)]

print(*[(len(list(g)), int(k)) for k, g in groupby(input())])
