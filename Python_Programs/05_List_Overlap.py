import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Uncomment the below for random values
# a,b = [random.sample(range(30), 4), random.sample(range(30), 4)]
c = []
# For each number of b, check if it is in a and not already in c

for numB in b:
    if(numB in a and not(numB in c)):
        c.append(numB)

print(c)
