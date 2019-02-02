''' This is a basic way to check if a number is prime '''


import math

def is_prime(n):
    # assert(isinstance(n, int)), 'The input must be > 0 and an integer'
    
    if n == 2:
        return True
    elif n % 2 == 0 or n < 2 or not isinstance(n, int):
        return False
    else:
        sqrt = round(n ** 0.5)
        for x in range(3, sqrt + 1, 2):
            if n % x == 0:
                return False
    return True


print(2, is_prime(2))
print(3, is_prime(3))
print(5, is_prime(5))
print(11, is_prime(11))
#print(is_prime(4329161))
print(is_prime(321.321321))



def primes_list_below(n):
    res = [2]
    for x in range(3, n + 1, 2):
        pass
    return 
