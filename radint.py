from random import randint

heads = 0
tails = 0

for trials in range(0, 1000000):
    while randint(0,1) == 0:
        tails = tails + 1
    heads = heads + 1

print("heads / tails = ", heads/tails)