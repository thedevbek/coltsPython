from random import randint
print('rock') 
print('paper') 
print('scissors')

player = input('Player: Make your move! ').lower()

rand_num = randint(0,2)
if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else: 
    computer = 'scissors'
print(f'Computer plays {computer}')

if player ==  computer:
    print("It's a tie!!")
elif player == 'rock': 
    if computer == 'scissors':
        print('You Wins!!')
    else:
        print('Computer Wins!!')
elif player == 'paper': 
    if computer == 'rock':
        print('You Wins!!')
    else:
        print('Computer Wins!!')
elif player == 'scissors': 
    
    if computer == 'paper':
        print('You Wins!!')
    else:
        print('Computer Wins!!')
    
else: 
    print('Please enter a valid move!')