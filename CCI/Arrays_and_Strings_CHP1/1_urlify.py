''' 
    Write a method to replace all spcaes in a string with "%20".
    EXAMPLE:
    Input: "Mr John Smith"
    Output: "MR%20John%20Smith"
'''



def urlify(string):
    ''' Python has a built in method for this called replace '''
    return string.replace(' ', '%20')



print('Testing our function:')

string1 = 'Mr John Smith'
string2 = ' G a b o r '
print('{} urlified --> {}'.format(string1, urlify(string1)))
print('{} urlified --> {}'.format(string2, urlify(string2)))

