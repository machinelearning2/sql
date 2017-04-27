from random import randint


total = 0
for toss in range(0, 100000):
    sum = randint(0,6)
    total = sum + total
    total = int(total)
average = total / 100000
print(average)

        