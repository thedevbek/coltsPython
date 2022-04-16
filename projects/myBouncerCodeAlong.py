#  ask for age
# 18-21 wristband
# 21+ drink, normal entry
# too young, sorry

## age = input('How old are you: ')
# if age != "":
#     if int(age)>= 18 and int(age) < 21:
#         print('You can enter, but need a wristband!')
#     elif int(age) < 17:
#         print('Too young, Go home!!')
#     else: print('Come on in!')
# else: print('Please enter your age!')
## Or
# age = input('How old are you: ')
# if age:
#     age = int(age)
#     if (age)>= 18 and (age) < 21:
#         print('You can enter, but need a wristband!')
#     elif (age) < 17:
#         print('Too young, Go home!!')
#     else: print('Come on in!')
# else: print('Please enter your age!')
## Or
age = input('How old are you: ')
if age:
    age = int(age)
    if age>= 21:
        print('Come on in!')
    elif age >= 18:
        print('You can enter, but need a wristband!')
    else: print('Too young, Go home!!')
else: print('Please enter your age!')