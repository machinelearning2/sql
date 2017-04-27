print("1 + 1 =", 1 + 1)
print("2 * (2 + 3) =", 2 * (2+3))
print("1.2 / 0.3 =", 1.2 / 0.3)
print("5 / 2 =", 5 / 2)

base = input("Enter a base:")
exponent = input("Enter an exponent:")
print(base, "to the power", exponent, "=", int(base)**int(exponent))


def cube(num):
    result = num**3
    return result

print(cube(7))


def multiply(num1, num2):
    mult = num1 * num2
    return mult

print(multiply(2,5))

