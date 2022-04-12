
# #! Number and Math
# # Integer are 4, -4, 0
# # Floating Point (Float) are 6.1, 1.333, 0.0

print(type(9)) # Integer
print(type(0.0))# Float
print(1/3) # division returns float, even when dividing two ints

# $ 10/3 = 3.3333 BUT if you use two // then you will get an integer.25//4 = 6

cash = 19867324678987.99  
print(cash // 5)

new_line = 'Hello\nworld'
print(new_line)
mountains = "/\\/\\/\\"
print(mountains )

# @ String Concatenation

str_one = 'Your'
str_two = 'Face'
str_three = print(str_one + '' + str_two) 

username = 'Bluthedog!'
print('Hello there and welcome to the game ' + username)

str_one = 'ice'
str_one += 'cream'
print(str_one)

# ! Formatting Strings
# # Current way
x = 10
formatted = print(f"I've told you {x} times already!")

guess = 8
print(f'Your guess of {guess} was incorrect!')

# # Older way
x = 10
formatted = print("I've told you {} times already!".format(10))

# # Deprecated way
x= 20
formatted = print("I've told you %d times already!" % (x))

first = 'Bek'
last = 'Johansson'

formatted = print('First Name: {}, Last Name: {}'.format(first, last))

decimal = 12.56345634534
integer = print(int(decimal))

my_list = [1, 3, 4]
my_list_as_a_string = print(str(my_list))

num = 12
num = print(float(num))

# print('Enter your name here:')
# name = input()
# print('Nice to meet you ' + name)

# print('What is your favorite color?')
# data = input()
# print('You said ' + data)

name = 'Arya Stark'
if name == 'Arya Stark':
    print('Valar Morghulis')
elif name == 'Jon Snow':
    print('You know nothing')
else:
    print('Carry on')

if 0: #Falsy
    print('Yay')

if 1: #Truthy
    print('Yay?')

# animal = input('Enter your favorite animal')

# if animal:
#     print(animal + ' is my favorite too!')
# else: 
#     print('Hello, animal?')
# Any string that isn't empty '' is Truthy!

# age = 6
# age > 2
# age < 8
# print(age > 2 and age < 8) 
# if age > 2 and age < 8:
#     print('You pay child price')

 # city = input('Where do you live?')

# if city == 'Los Angeles' or city == 'San Francisco':
#     print('You live in California!')
# else:
#     print("You don't live in California!!")

age = 2
#2-8 $2 ticket
#65 $5 ticket
# 10 dollars for everyone else

if not((age >= 2 and age <= 8) or age >= 65):
    print('You pay full price')
else: 
    print('You have a discount!')

x = 13
y = 13
print(x == y) #True
print(x is y)

a = [1,3]
b = [1,3]
print(a == b) #True
print(a is b) #False

clone = a
print(a is clone) #True