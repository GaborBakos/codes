''' 
    Implement a method to perform basic string compression using the counts of repeated characters.
    EXAMPLE:
    Input: aabcccccaaa
    Output: a2b1c5a3

    If the "compressed" string would not become smaller than the original return the original.
    You can assume the string has only uppercase and lowercase letters (a-z).
'''

def compress(string):
    new_string = string[0]
    count = 1

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count+=1
        else:
            new_string += str(count)
            new_string += string[i+1]
            count = 1
    new_string += str(count)
    
    if len(new_string) >= len(string):
        return string
    return new_string



print('Testing:')


string1 = 'aabcccccaaa'
string2 = 'bbbgaobgoaoaooooooooooooooooooooooooooooooog'
string3 = 'goahgnpajngpangoinsokgnobng'
print('{} --> {}'.format(string1, compress(string1)))
print('{} --> {}'.format(string2, compress(string2)))
print('{} --> {}'.format(string3, compress(string3)))





