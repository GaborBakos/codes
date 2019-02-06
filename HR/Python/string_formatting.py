'''
	Given an integer, n, print the following values for each integer i from 1 to n:
	Decimal
	Octal
	Hexadecimal (capitalized)
	Binary
	The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of .
'''



def print_formatted(number):
    length = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        #print('{0:{length}} {0:{length}o} {0:{length}X} {0:{length}b}'.format(i, length=length))
        print('{0:.<{length}} {0:.^{length}o} {0:.>{length}X} {0:*<{length}b}'.format(i, length=length))
# The above isnt aesthetic but rather just a demostration of the different alignments we can do.


if __name__ == '__main__':
    n = 255
    print_formatted(n)
