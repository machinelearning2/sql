def divide_evenly(num):
    for n in range(1,(num+1)):
        if num % n == 0:
            print(n, "is a divisor of", num)


num = input("Enter a positive integer:")
num = int(num)

divide_evenly(num)


