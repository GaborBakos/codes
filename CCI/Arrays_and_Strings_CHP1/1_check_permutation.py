''' Given two strings, write a method to decide if one is a permutation of the other. '''


def is_permutation(string1, string2):
    d1 = {}
    d2 = {}

    for char in string1:
        d1[char] = d1.get(char, 0) + 1
    for char in string2:
        d2[char] = d2.get(char, 0) + 1
    
    for key, value in d1.items():
        if d2.get(key) != value:
            return False
    return True


''' This function can be created with built in functions as well, but if you want to show full working this might be an easy implementation. '''

from collections import Counter

def is_perm_coll(string1, string2):
    c1 = Counter(string1)
    c2 = Counter(string2)
    if c1 == c2:
        return True
    return False



print('Testing out the above functions')


str1 = 'Gabor'
str2 = 'Gbaor'
str3 = 'gabor'
str4 = '1234567890'
str5 = '0987654321'

str_list = [str1, str2, str3, str4, str5]
print('We will test the function we wrote')
print('Is {} permutation of {} : {}'.format(str1, str2, is_permutation(str1, str2)))
print('Is {} permutation of {} : {}'.format(str1, str3, is_permutation(str1, str3)))
print('Is {} permutation of {} : {}'.format(str2, str3, is_permutation(str2, str3)))
print('Is {} permutation of {} : {}'.format(str4, str5, is_permutation(str4, str5)))


print('\n\n\n')
print('We will test out the version which uses the collection\' Counter method')
print('Is {} permutation of {} : {}'.format(str1, str2, is_perm_coll(str1, str2)))
print('Is {} permutation of {} : {}'.format(str1, str3, is_perm_coll(str1, str3)))
print('Is {} permutation of {} : {}'.format(str2, str3, is_perm_coll(str2, str3)))
print('Is {} permutation of {} : {}'.format(str4, str5, is_perm_coll(str4, str5)))


print('We can see that this is case sensitive search, we can modify this by adding char.lower() to our code')








