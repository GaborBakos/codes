''' Is Unique: implement and algorithm to determine if a sting has all unique characters. What if you cannot use additional datastructures? '''

def is_unique(string):
    ''' We use a dictionary to determine if a given character has occured more than once in the string. '''
    d = {}
    for char in string:
        d[char] = d.get(char, 0) + 1
        if d[char] > 1:
            return False
    return True


print('Testing the "is_unique" function with couple examples')

str1 = 'Gabor'
str2 = 'abba'
str3 = 'abcdefga'
str4 = '1234567890abcdefgh'
str5 = 'gponaoign0iningoinosnbpomf2-j-32jg-n'
str_list = [str1, str2, str3, str4, str5]

for string in str_list:
    print('"{}" --> {}'.format(string, is_unique(string)))




def is_unique_nd(string):
    ''' We use two for loops to determine if there are any duplicates, the first loop goes over all characters, the second one goes from the commencing index to the last. '''
    for index, char in enumerate(string):
        if index < len(string):
            for sub_char in string[(index+1):]:
                if char == sub_char:
                    return False
    return True

print('\n\n\n')
print('Testing the "is_unique_nd" function with couple examples')

str1 = 'Gabor'
str2 = 'aba'  #testing for edge case first and last element.
str3 = 'abcdefga'
str4 = '1234567890abcdefgh'
str5 = 'gponaoign0iningoinosnbpomf2-j-32jg-n'
str_list = [str1, str2, str3, str4, str5]

for string in str_list:
    print('"{}" -->  {}'.format(string, is_unique_nd(string)))



