# class about Dogs


class Dog(object):

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):

        self.name = name
        self.age = age

# Instantiate the Dog object
ares = Dog("Ares", 4)
pooch = Dog("Pooch", 7)
fido = Dog("Fido", 3)


# Determine the oldest dog
def get_biggest_number(*args):
    return max(args)

# output
print("The oldest dog is {} years old.".format(
    get_biggest_number(ares.age, pooch.age, fido.age)))
