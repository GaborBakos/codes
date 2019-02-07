def probability_given(n):
    res = 1
    for i in range(n):
        res *= (365 - i)
    res /= 365 ** n
    return 1.0 - res


if __name__ == '__main__':
    for n in range(100):
        print('{}, probability of at least one matching birthday: {}'.format(n, probability_given(n)))
