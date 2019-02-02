'''
    Given a string write a function to check if it is a permutation of a palindrome.
    A palidrome is a word or phrase that is the same forwards and backwards. 
    A permutation is rearrangement of letters. 
    The palindrome does not need to be limited to just dictionary words.
'''

print('We will utilize the string module to remove any punctuations from the sentences.')

import string
translator = str.maketrans('', '', string.punctuation)


def palindrome_permutation(st):
    d = {}
    st = st.translate(translator).replace(' ','')
    count_odd = 0
    for char in st:
        d[char.lower()] = d.get(char.lower(), 0) + 1
    for key, value in d.items():
        if value % 2 == 1:
            count_odd += 1
    if count_odd % 2 == 1 and count_odd < 2:
        return True
    return False





print('Testing out our function')


string1 = 'Taco Cat'
string2 = 'gabor'
string3 = 'A man, a plan, a canal: Panama'
print('{} palindrome permutation --> {}'.format(string1, palindrome_permutation(string1)))
print('{} palindrome permutation --> {}'.format(string2, palindrome_permutation(string2)))
print('{} palindrome permutation --> {}'.format(string3, palindrome_permutation(string3)))



