#Convert temperatures


def celsius(f):
    c = (f-32)*5/9
    return c

def fahrenheit(c):
    f = c*9/5 + 32
    return f

f = input("Enter degrees in fahrenheit")
f = int(f)
print(celsius(f))

c = input("Enter degrees in celsius")
c = int(c)
print(fahrenheit(c))