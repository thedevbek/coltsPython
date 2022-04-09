# !Variables

city = 'Brownsville' # string is str in Python
price = 1.3 # a float is a decimal number
high_score = 3 # int is a number that is not a decimal number
is_having_fun = True

# ! String Escape Characters
# are metacharacters they get intrpreted by python to do something special
#@ \n  new line
new_line = 'hi\nthere!'

#@ \\ is how you make a backslash
back_lash = 'this is a backslash \\'

#@ You can use a backslash if you don't want to change up '' to ""
quotation = 'My cat said \'meow\'!'

# ! String Concatenation

greeting = 'Hello'
name = 'Colt'
greet_Name = greeting + '' + name

# you can also write it like this 
greet = 'Hi'
greet += 'Colt'

# @ Formatting Strings interpolation variables which is putting str and nums together
# The new way
x = 10
formatted = f"I've told you {x} times already"

# Old way

x = 20
formatted = "I've told you {} times already!".format(20)

# Deprecated way

x = 30
formatted = "I've told you %d times already" %(x)

first = 'Bek'
last = 'Johansson'

formatted = 'First Name: {}, Last Name: {}'.formatted(first, last)

first = 'Colt'
last = 'Steele'

formatted = f'First Name: {first}, Last Name: {last}'

# # Coverting Data Types
#changing nums = '3' into a number

decimal = 12.56345634534
integer = int(decimal)
#chops off decimal DOESN'T ROUND

#!str turns things int to a string
my_list = [1,2,3]
my_list_as_a_string = str(my_list) 

str(8) #'8'

input() #user input box


