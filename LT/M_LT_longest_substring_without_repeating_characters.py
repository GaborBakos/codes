'''
    Given a string, find the length of the longest substring without repeating characters.
    Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.\
    Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:
    Input: "pwwkew"
    Output: 3
    Explanations: The answer is "wke", with the length of 3.
                    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


# The below solutions is super inefficient, it is of O(n^3)
def isUnique(string):
    d = {}
    for char in string:
        d[char] = d.get(char, 0) + 1
    for key, value in d.items():
        if value > 1:
            return False
    return True


def lengthOfLongestSubstring(string):
    length = 0 if len(string) == 0 else 1
    for x in range(2, len(string) + 1):
        for i in range(len(string) - x + 1):
            d = {}
            substring = string[i:i+x]
            if isUnique(substring):
                length = len(substring)
    return length


print('Testing our function:')
str1 = 'abcabcbb'
str2 = 'bbbbb'
str3 = 'pwwkew'
str4 = 'Gabor'
str5 = 'abcdefghijklmnopqrstuvwzyzabcd1234567890'
print('{} has longest substring of length {}'.format(str1, lengthOfLongestSubstring(str1)))
print('{} has longest substring of length {}'.format(str2, lengthOfLongestSubstring(str2)))
print('{} has longest substring of length {}'.format(str3, lengthOfLongestSubstring(str3)))
print('{} has longest substring of length {}'.format(str4, lengthOfLongestSubstring(str4)))
print('{} has longest substring of length {}'.format(str5, lengthOfLongestSubstring(str5)))



# For a more roboust linear time function we need to think a bit more carefully



def longest(string):
    d, res, start = {}, 0, 0
    # we start by going through the string character by character
    for index, char in enumerate(string):
        # if a given character is already in the dictionary we will modify the result and our start
        if char in d:
            # the new result will be the maximum of previous result vs the length of the currently inspected substring
            res = max(res, index - start)
            # the new start will be the maximum of previous start vs the index of our character + 1 (getting rid of the duplicated character for the next iteration 
            start = max(start, d[char] + 1)
        # we set the value of our character to be the index where it appears or update the previous value to the current index
        d[char] = index
    # the result is either at the can be at start middle or the end of the string
    return max(res, len(string) - start)



print(longest('Gabor'))
print(longest('abcdefghijklmnopqrstuvwzyzabcd1234567890'))

