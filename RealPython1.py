# This is my first script
phrase = "Hello, World"
print(phrase)

phrase2 = "This is practice"
print(phrase2)

my_string = "abcdef"
string_length = len(my_string)
print(string_length)

string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
print(magic_string)

print("abra", "ca", "dabra")

flavor = "birthday cake"
print(flavor[3])

print(flavor[0])

print(flavor[0:3])

print(flavor[:5])

print(flavor[5:])

print(flavor[:])

my_string = "goal"
my_string ="f" + my_string[1:]
print(my_string)

my_string = "bazinga"
my_string = my_string[2:6]
print(my_string)

user_input = input("hey, what's up?")
print("You said: ", user_input)

response = input("What should I shout? ")
response = response.upper()
print("Well, if you insist...", response)

password =input("Tell me your password")
password = password.upper()
password =print(password[0])

my_number = "12"
print (int(my_number))

print (float(my_number))

string_object = "8"
string_object = int(8)
string_object = 7 * string_object
print(string_object)

string_object2 = "houses"
int_object = int(15)
print("Our block has", str(int_object), string_object2)

weight = float(0.2)
animal = "newt"
print(weight, "kg is the weight of the", animal)
print("{heavy} kg is the weight of the {type}" .format(heavy=float(0.2), type="newt"))

print("{0} kg is the weight of the {1}" .format(weight, animal))

print("AAA".find("a"))

value = "version "
float_value = float(2.0)
string_value = f"float_value"
final_value = value + string_value
first_occurrence = final_value.find(string_value)
print(first_occurrence)

password = input("Tell me your password")
print(password.find("f"))

sentence = input("Enter some text:")
new_sentence = sentence.replace("a", "4")
new_sentence = new_sentence.replace("b", "8")
new_sentence = new_sentence.replace("e", "3")
new_sentence = new_sentence.replace("l", "1")
new_sentence = new_sentence.replace("o", "0")
new_sentence = new_sentence.replace("s", "5")
new_sentence = new_sentence.replace("t", "7")

print(new_sentence)
