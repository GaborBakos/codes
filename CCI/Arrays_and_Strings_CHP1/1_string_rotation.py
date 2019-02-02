'''
    Assume you have a method isSubstring which cheks if one word is a substring of another.
    Given two strings, s1 and s2, write a code to check if s2 is a rotation of s1 using only one call to isSubstring.
    EXAMPLE:
    "watterbottle" is a rotation of "erbottlewat"
'''

print(
''' 
Lets first create the method isSubstring
so in the above example we can see if we call waterbottle as x and erbottlewat as y
y+y will be erbottlewaterbottlewat which contains the waterbottle substring
we will use this observation to create the function is_substring(s1, s2)
'''
)

def is_substring(s1, s2):
    s1 = s1 + s1
    if s2 in s1:
        return True
    return False

print('Testing the above function')

s1 = 'erbottlewat'
s2 = 'waterbottle'
s3 = 'robaag'
s4 = 'gabor'
print('Is {} a rotation of {} --> {}'.format(s1, s2, is_substring(s1, s2)))
print('Is {} a rotation of {} --> {}'.format(s3, s4, is_substring(s3, s4)))







