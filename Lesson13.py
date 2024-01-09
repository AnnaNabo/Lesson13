import random

def pech(mas):
    for Str in mas:
        print(Str)

a = int(input())
b = int(input())
mas1 = [] 
mas2 = []


mas1 = [[random.randint(0, 100) for j in range(a)] for i in range(b)]
mas2 = [[random.randint(0, 100) for j in range(a)] for i in range(b)]
mas3 = [[0 for j in range(a)] for i in range(b)]


for i in range(b):
    for j in range(a):
        mas3[i][j] = mas1[i][j] + mas2[i][j]

print("mas1:")
pech(mas1) 
print("mas2:")
pech(mas2)
print("mas3:")
pech(mas3)