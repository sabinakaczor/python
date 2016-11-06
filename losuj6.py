import random

A = []
for i in range (0,6):
    random.seed()
    k = random.randint(1, 45)
    while (k in A):
        k = random.randint(1,45)
    A.append(k)

print A


