'''
    This is a small collection of algorithms that I found interesting during coding.
'''

def highest_substring_sum(lst):
    '''
        Finding the highest sum of all substrings in a list.
        The algorithms is based on Kadane's algorithm.
        It solves this problem in O(n) and can solve the problem in 
        the case when all elements are -ve.        
    '''
    if not lst:
        return

    current_max = lst[0]
    maximum = lst[0]

    for value in lst:
        current_max = max(value, current_max + value)
        maximum = max(maximum, current_max)

    return maximum


print('Testing:')

lst = [-1,-2,-3,-4,-5,10,12,-321,21,-4,-5,-6,-7,-8,12,8]
print(lst)
print('What is the highest sum of a substring in the above list?')
print(highest_substring_sum(lst))
