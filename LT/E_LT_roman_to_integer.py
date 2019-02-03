'''
    Translate Roman numerals translated to integers.
'''

def roman_to_int(s):
    res = 0
    d = dict(M=1000, D=500, C=100, L=50, X=10, V=5, I=1)
    special_cases = dict(CM=900, CD=400, XC=90, XL=40, IX=9, IV=4)

    for key, value in special_cases.items():
        if key in s:
            s = s.replace(key, '')
            res += value
    for char in s:
        res += d[char]

    return res



print('Testing')
roman = 'MMCMXLV'
print('{} is {}'.format(roman, roman_to_int(roman)))
