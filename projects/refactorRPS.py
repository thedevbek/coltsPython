print('rock') 
print('paper') 
print('scissors')

player1 = input('Player 1: Enter rock, paper, or scissors!')
player2 = input('Player 2: Enter rock, paper, or scissors!')

if player1 ==  player2:
    print("It's a tie!!")
elif player1 == 'rock': 
    if player2 == 'scissors':
        print('Player 1: Wins!!')
    elif player2 == 'paper':
        print('Player 2: Wins!!')
elif player2 == 'rock': 
    if player1 == 'scissors':
        print('Player 2: Wins!!')
    elif player1 == 'paper':
        print('Player 1: Wins!!')
else: 
    print('Something went wrong')
