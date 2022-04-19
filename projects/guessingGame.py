import random
num = random.randint(1,10)
## input Guess a number between 1 and 10 
## if statement that says You guess it, you won, too low, too high, try again.
## make it a random number
## put in do you want to play again? (y/n)


guess = print(int(input(("Guess a number between 1 and 10! "))))
num = print(random.randint(1,10))

# if num == guess:
#     print('You guessed it!')
# else: 
#     print('Fuck You')
## look up continue it continues game?
while guess == num:
    print('You guess it!!')
    break
# if  num <= 5:
#     print('Too low, try again')
# elif num >= 6:
#     print('Too high, try again')
# print(num)

# age = int(random.randint(1,10))
# if age == 3:
#     print('same')
# else:
#     print('different')