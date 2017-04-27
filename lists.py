#Lists

desserts = ["ice cream", "cookies"]

desserts.sort()
print(desserts)

print(desserts.index("ice cream"))

food = []
food.extend(desserts)
print(food)

food.extend(["broccoli", "turnips"])
print(food)
print(desserts)

food.remove("cookies")
print(food)

print(food[0:2])

sweets = "cookies, cookies, cookies"
breakfast = sweets.split(",")
print(sweets)
print(breakfast)


def list_numbers():
    for n in range(0,5):
        num = list_numbers.index[n]
        if num > 1 and num < 20:
            print(num)

nums1 = [2,4,8,16,32,64]
print(list_numbers(nums1))

