'''
    Given a string s, find the longest palindromic substring in s. 
    You may assume that the maximum length of s is 1000.
    Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer
    Example 2:
    Input: "cbbd"
    Output: "bb"
'''


def longest_palindrome(s):
    ''' Not efficient, but a good first try. '''
    palindromes_list = []
    longest = s[0]
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in palindromes_list:
                pass
            elif s[i:j] == s[i:j][::-1]:
                palindromes_list.append(s[i:j])
    for el in palindromes_list:
        if len(el) > len(longest):
            longest = el
    return longest

def dplongestPalindrome(s):
    ''' Here we use dynamic programming, we will store results in a table to 
        find the longest palindrome. The table will store the following information:
        t[i][j] = True --> the substring starting at index i and ending at index j
        is a palindrome. 
    '''
    lens = len(s)
    if lens == 0:
        return ""

    # Initialize the table
    t = [[False for i in range(lens)] for j in range(lens)]

    start = 0 # The index of the longest palindrome
    max_len = 1 # Maximum length of the palindrome (a letter by itself is a palindrome so we start with 1)

    for i in range(lens):
        t[i][i] = True

    for i in range(lens - 1):
        j = i + 1
        if s[i] == s[j]:
            t[i][j] = True
            start = i
            max_len = 2

    length = 3
    while length <= lens:
        for i in range(lens - 2):
            j = i + (length - 1)
            if j < lens: # if calculated j is a valid value
                if s[i] == s[j] and t[i+1][j-1]:
                    t[i][j] = True
                    start = i
                    max_len = length
        length += 1

    solution = s[start: start + max_len]

    return solution

def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]


print('Testin:')

str1 = 'babad'
str2 = 'cbbd'
print('Longest palindrome of {} is {}'.format(str1, longest_palindrome(str1)))
print('Longest palindrome of {} is {}'.format(str2, longest_palindrome(str2)))
print('Longest palindrome of {} is {}'.format(str1, longestPalindrome(str1)))
print('Longest palindrome of {} is {}'.format(str2, longestPalindrome(str2)))





