'''
    Find the longest common prefix of a list of strings.
'''

def longest_common_prefix(list_of_strings):
    if not list_of_strings:
        return ''

    maximal_prefix = min(list_of_strings, key=len)

    for index, char in enumerate(maximal_prefix):
        for string in list_of_strings:
            if string[index] != char:
                return maximal_prefix[:index]
    return maximal_prefix


print('Testing:')


strs = ['flower', 'flow', 'flight']

print('{} --> {}'.format(strs, longest_common_prefix(strs)))
