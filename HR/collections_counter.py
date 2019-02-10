'''
 Task

AA is a shoe shop owner. His shop has N number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money AA earned.

Input Format

The first line contains N, the number of shoes. 
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains M, the number of customers. 
The next M lines contain the space separated values of the shoe size desired by the customer and x_i, the price of the shoe.
'''


from collections import Counter

N = int(input())
shoes = [int(el) for el in input().split(' ')]
d = Counter(shoes)
M = int(input())
MONEEEY = 0
for _ in range(M):
    size, money = [int(el) for el in input().split(' ')]
    if d[size] > 0:
        MONEEEY += money
        d[size] -= 1
print(MONEEEY)
