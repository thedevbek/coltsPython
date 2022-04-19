
# ##Number and Math
# ## Everything gets stored in memory because of 1 and 0, so it's all about space.


# num=(1,4) ## integer
# num=(1.3333, 6.1) ## Floating Point (Floats)

# print(type(3.1)) ## give type 

# ## Math operators
# ##  + = addition, - subtract, * multiply, / division (with decimals),// division (floor which is rounding down #),  ** exponentiation, % modulo ( gives the remainder, creates even % 2 and odd % 1)


## variables

# x = 100 
# khaleesi_mother_of_dragons = 1
# print(khaleesi_mother_of_dragons + x)

# ## variables are always assigned with the variable name on the left and the value on the right of the = . Variables must be assigned before they can be used. Variables can be assigned to other variables, reassigned at any time, and assigned at the same time as other variables if it makes since.

# python_is_awesome = 100
# just_another_var = python_is_awesome
# python_is_awesome = 1337
# all, at, once = 5, 10, 15
# print(once) ## give me 15 cause once = 15 only makes sense

## Data Types 
# bool = True or False values
# int = an integer (1,2,-3)
# str = 'string'  a sequence of Unicode characters, e.g. 'Colt'
# list = an ordered sequence of values of other data types, e.g. [1,2,3]
# dict = a collection of key:values, eg. {'first_name': 'Bek', 'last_name':'Johansson'}
# \newline = \n, to use a backslash \\, \'single\'

# game_over = False
# null = None

## String Concatenation Functions

# str_one = 'Bek'
# str_two = 'Johansson'
# str_three = str_one  + ' ' + str_two
# print(str_three)

# cream = 'ice'
# cream += ' cream' ## can also use - and *
# print(cream)

## Formatting strings
## There are also several ways to format strings in Python to interpolate variables.

## F-string
# x = 100
# formatted = f'I\'ve told you {x} times already!'
# print(formatted)
## (Python 2 -> 3.5 => .format method)
# formatted = 'I\'ve told you {} times already!'.format(10)
# print(formatted)
## Deprecated way of fromatting strings 
# formatted = 'I\'ve told you %d times already!' %(3893) 
# print(formatted)

# answer = 'yaaaaaaaaa'
# print(answer[0])

# ## Converting Data types with int() and str()
# decimal = 12.56345783
# integer = int(decimal)
# print(integer)

# my_str = 1
# full = str(my_str)
# print(type(my_str))
# my_list = [1, 2, 3]
# my_list_as_a_string = str(my_list)
# print(type((my_list_as_a_string)))

################# MILES CONVERTER ############################

# kms = input(('How many kilometers did you run today?'))
# miles = float(kms)/1.60934
# print(f'Your {kms} kms ride was in {round(miles, 2)} miles! ')
###############################################################

##Conditional Statements
## Conditional logic using if statements represents different paths a program can take based on some type of comparison of input.

##  if some condition is True:
##    do something
##  elif someth other condition is True:
##    do something
##  else: 
##    do something

# name=''
# if name == 'Arya Stark':
#     print('Valar Morghulis')
# elif name == 'Jon Snow':
#     print('You know nothing')
# else: print('Who are you?')

# from random import randint
# choice = randint(1,10)

# choice = 7
# if choice == 7:
#     print('You are lucky!')
# else: print('You are not so lucky!')

# num = int(input('Enter a number: '))
# if (num % 2) == 0:
#      print('Even')
# else: print('Odd')
## can also be written like this
# num = int(input('Enter a number: '))
# if num % 2 != 0:
#     print('Odd')
# else: print('Even')

## Truthy and Falsy
## Beside False conditional checks, other things that re naturally falsy include: empty objects, empty strings, None, and zero. Everything else is Truthy!!!!

# from random import choice
# food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])

# food = input('What do you want?')
# if food == 'apple' or food =='grape':
#     print('fruit')
# elif food == 'bacon' or food == 'steak':
#     print('meat')
# else:
#     print('Yuck')

################# Bouncer Code-Along ##########################

# age = input('How old are you? ')
# if age != '':
#     age = int(age)
#     if age >= 21:
#         print('Enjoy!')
#     elif age >= 18:
#         print('Wristband!')
#     else: print('Go Home!')
# else: print('Please enter age: ')
################################################################
# # NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!! (please)         
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /
x = 84
y = -12
if x > 0 and y > 0:
    print("both positive")
elif x  < 1 and y < 1: 
    print('both negative')
elif  not x > 0 and y < 0: 
    print("x is positive and y is negative")
else: 
    print("y is positive and x is negative")
###################################################
# NO TOUCHING ======================================

# from random import choice, randint

# # randomly assigns values to these four variables
# actually_sick = choice([True, False])
# kinda_sick = choice([True, False])
# hate_your_job = choice([True, False])
# sick_days = randint(0, 10)
# # _NO TOUCHING ======================================
# calling_in_sick = True  # set this to True or False with Boolean Logic and Conditionals!
# if actually_sick and sick_days > 0 :
#     calling_in_sick = True
# elif kinda_sick and sick_days and hate_your_job > 0:
#     calling_in_sick = True
# else: 
#     calling_in_sick = False
# ################################################################
#################Rock, Paper, Scissors vs1################
