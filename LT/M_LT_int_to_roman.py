''' 
    Convert int to Roman number.
'''



'''
Initial brute force, going through the cases:
    d = dict(M=1000, D=500, C=100, L=50, X=10, V=5, I=1)
        d = {value: key for key, value in d.items()}
        special_cases = dict(CM=900, CD=400, XC=90, XL=40, IX=9, IV=4)
        special_cases = {value: key for key, value in special_cases.items()}

        ones = num % 10
        tens = num % 100 - ones
        hundreds = num % 1000 - tens - ones
        tousands = num % 10000 - hundreds - tens - ones

        res = ''

        if tousands:
            times = tousands / 1000
            res += d[1000] * int(times)


        if hundreds in special_cases.keys():
            res += special_cases[hundreds]
        else:
            if hundreds >= 500:
                res += 'D'
                hundreds -= 500
                times = hundreds / 100
                res += d[100] * int(times)
            else:
                times = hundreds / 100
                res += d[100] * int(times)

        if tens in special_cases.keys():
            res += special_cases[tens]
        else:
            if tens >= 50:
                res += 'L'
                tens -= 50
                times = tens / 10
                res += d[10] * int(times)
            else:
                times = tens / 10
                res += d[10] * int(times)

        if ones in special_cases.keys():
            res += special_cases[ones]
        else:
            if ones >= 5:
                res += 'V'
                ones -= 5
                res += d[1] * int(ones)
            else:
                res += d[1] * int(ones)

        return res
'''
# A much more elegant solution can be done by using a sorted list of tuples

sorted_int_roman = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')]


def int_to_roman(num):
    '''
        We have an ordered list of tuples of integers with corresponding roman numerals.
        We loop through this list and compare the integer part with our number.
        If the number is larger than the integer, we will add to our result
        the corresponding number of roman numerals.
        Then replace our num with the num mod integer and carry on with our iteration.
    '''
    res = ''
    for integer, roman_rep in sorted_int_roman:
        if num >= integer:
            res += roman_rep * (num // integer)
            num %= integer
    return res


print('Testing:')

num1 = 1992
num2 = 1492
num3 = 3999
num4 = 1567
num5 = 2019
print('{} --> {}'.format(num1, int_to_roman(num1)))
print('{} --> {}'.format(num2, int_to_roman(num2)))
print('{} --> {}'.format(num3, int_to_roman(num3)))
print('{} --> {}'.format(num4, int_to_roman(num4)))
print('{} --> {}'.format(num5, int_to_roman(num5)))










