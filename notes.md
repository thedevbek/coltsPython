<!-- ! OS File Structure -->

/ is the root directory

folders are in a hierarchy (a tree)

Files and diretories have <!--!absolute paths
based on the root where each additional level down adds a '/'. <!--!Example /User/bek/Desktop

<!--% The green -->

directory below is a special directory called 'home', which is also known as '~'Tilde. This is the default directory upon open your terminal.

<!--@ PWD (print working directory-->

PWD will tell you the full absolute path of where you are at!

<!--@ CD (Change directory) -->

followed by the <!--$absolute path-->
of the folder will navigate you directly there. Example cd /Users/bek will get me to my bek folder from where ever I am.

<!--@ The dot '.'-->

stands for current directory and dot-dot '..' stands for parent directory. This allows for <!--@ relative navigation-->
'..' dot-dot take you back to the last level.

<!--@ ls stand for 'list'-->

The keyword 'ls' will 'list' the contents of a directory. You can supply options such as '-a' to list all files (including hidden ones), or '-l' for a longer format.

<!--@ mkdir ('make directory'-->

The command 'mkdir' followed by the name of the new directory will create a new child directory inside the current directory. The child

<!--@ 'touch' creates new files-->

The command 'touch' followed by the filename and file-type extension will create a new file of that type.

example: touch favs.txt

<!--@ 'mv' moves or renames files-->

Files can be moved or renamed using the 'mv'('move') keyword, which takes two arguments: the source and the destination.

<!--$ 'rm'removes files files-->

When its gone its gone!!

<!--$ 'rm -rf'removes directories files-->

Directories can also be deleted using the 'rm' keyword, with the added option '-r'('recursive'). You can also use '-f' ('force') to prevent warnings.

<!--# example: rm -rf 'directory'

<!--% Dynamic Typing -->

Python is highly flexible about reassigning variables to different types: boolean to a string to a number to none. This is called dynamic typing since variables can change easily. Other languages like C++, are statically-typed and variables are stuck with their originally-assigned type.

<!--! String Escape Characers -->

In Python there are also 'escape characters', which are 'metacharacters' - they get interpreted by Python to do something special: 1) How to make a return in string \n 2) How to make a backslash \\

<!-- $ Formatting Strings -->

There are also several ways to format strings in Python to <!-- $ Interpolate--> variables.
The new way (new in Python 3.6) =>F-Strings
x = 10
formatted = f"I've told you {x} times already!"

<!-- # Format method -->

x = 10
formatted = 'I've told you {} times already!'.format(10)

<!-- @ Deprecated Format method -->

x= 20
formatted = print("I've told you %d times already!" % (x))

<!-- !Converting Data Types -->

In string interpolation, data types are IMPLICITLY converted into string form

You can also EXPLICITLY CONVERT variables by using the name of the builtin type as a function -- int and str

decimal = 12.56345634534
integer = int(decimal)

<!-- @ int removes the decimal and makes it 12 but DOES NOT ROUND -->

my_list = [1, 3, 4]
my_list_as_a_string = str(my_list)

<!-- # str makes everything a string by putting '' around it  -->

num = 12
num = float(num)

<!-- !Turn the num into a decimal also when divide by is used it's a float -->

<!-- % Boolean and Conditional Logic -->

There is a built-in function in Python called "input" that will prompt the user and store the result to a variable. input()

<!-- ! Conditional Statement -->

Conditional logic using if statements represents different paths a program can take based on some type of comparison of input.

if some condition is True:
(must have tab here)do something
elif (you can sue elif as man times as you like) some other condition is True:
do something
else:
do this

<!-- ! Truthiness and Falseness -->

In python, all conditional checks resolve to True or False.

x = 1
x is 1 #True = truthy
x is 0 #False = falsy

Beside False conditional checks other things that are <!--! naturally falsy-->
include: empty objects, empty strings, None, and zero.

<!--% Conditional Logic Statements  -->

Using if statements represents different paths a program can take based on some type of comparison of input.

'if, elif, else'

<!-- # Comparison Operators -->
<!-- $ a = 1 and b = 1 -->

== Truthy if a has the same value as b

<!-- ! a == b #True -->

!= Truthy if a does NOT have the same value as b

<!-- ! a != b #False -->

> Truthy if a is greater than b

<!-- ! a > b #False -->

< Truthy if a is less than b

<!-- ! a < b #False -->

> = Thruthy if a is greater than or equal to b

<!-- ! a >= b #True -->

<=Truthy if a is less than or equal to based on

<!-- ! a <= b #True -->

<!-- @ Logical Operators put in if statement -->

In Python, the following operators can be used to make Boolean Logic comparisons or statements.

<!-- $ and -->

Truthy if both a AND b are true (logical conjunction)

<!-- % and example -->

if a and b:
print(c)

<!-- $ or -->

Truthy if either a OR b are true (logical disjunction)

<!-- % or example -->

if am_tired or is_bedtime:
print('go to sleep')

<!-- $ not -->

Truthy if the opposite of a is true (logical negation)

<!-- % not example -->

if not is_weekend:
print('go to work')

<!-- ! is vs. '==' -->

== and is are very similar comparators, however they are not the same.
a = 1
a == 1 #True Value
a is 1 #True Memory (===)

a = [1,2,3] # a list of nums
b = [1,2,3]
a == b #True
a is b #True

c = b
b is c #True

<!-- ! b is pointing to c in memory  or it's like === shows exactly where it is and the value-->

<!-- # LOOPS -->

Collection of data we can loop through!
We want to do something <!-- % FOR this data-->

#for# item #in# iterable_object: # do something with item

<!-- ! for and in is the syntax for python -->

1. An iterable object is some kind of collection of items, for instance: a list of numbers, a string of characters, a range, ect.
2. it is a new variable that can be called whatever you want
3. item references the current position of our iterator within the iterable. It will iterate over (run through) every item of the collection and then go away when it has visited all items.

<!-- @ ranges -->

If we just want to print numbers, we can simply iterate over a range. A range is just a slice of the number line. Python ranges come in multiple forms:

1. range(7) gives you intergers from 0-6 because the count starts at 0 since we put only 1 number in it and then it goes to 7 -1
2. range(1,8) will give you integers from 1 to 7 because two parameters are (start, finish)
3. range(1,10,2) will give you odds from 1 to 10 because the Third param is called the 'step', meaning how many to skip. But it can also tell you which direction to go to up or down if you have a range(1,10,-1) negative number in the step parameter.

<!-- !! while loops -->
<!--$ You can do more with a while loop than you can with a for loop

We can also irerate using a while loop, which has a different format:
        while im_tired:
            #seek caffeine
while loops continue to execute while a certain condition is truthy, and will end when they become falsy.
        user_response = None
        while user_response != 'please':
            user_response = input('Ah ah ah, you didn't say the magic word: ')
while loops require more careful setup than for loops, since you have to specify the termination conditions manually.
<!-- % Be careful!! If the condition doesn't become false at some point, your loop will continue FOREVER!! -->

<!-- # Controlled Exit -->

The keyword break gives us the ability to exit out of while loops whenever we want:
While True:
command = input('Type "exit" to leave: ')
if (command == 'exit'):
break

We an also use it to end for loops early:
for x in range(1, 101):
print(x)
if x == 3:
break
