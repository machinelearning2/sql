def invest(amount,rate,time):
    print("principal amount:",amount)
    print("annual rate of return:",rate)
    time = int(time) + 1
    for n in range(1,time):
        amount = amount * 1.05
        print("year",str(n)+":","$"+str(amount))

invest(100, .05, 8)


uword = input("Please enter word:")
uword = str(uword)
length = len(uword)
if length < 5:
    print("length is less than 5")
elif length > 5:
    print("length is greater than 5")
else:
    print("length is equal to 5")
