print('rock') 
print('paper') 
print('scissors')

player1 = input('Player 1: Enter rock, paper, or scissors!')
player2 = input('Player 2: Enter rock, paper, or scissors!')

if player1 == 'rock' and player2 == 'scissors':
    print('Player 1: Wins!!')
elif player1 == 'paper' and player2 == 'rock':
    print('Player 1: Wins!!')
elif player1 == 'scissors' and player2 == 'paper':
    print('Player 1: Wins!!')
elif player2 == 'paper' and player1 == 'rock':
    print('Player 2: Wins!!')
elif player2 == 'scissors' and player1 == 'paper':
    print('Player 2: Wins!!')
elif player2 == 'rock' and player1 == 'scissors':
    print('Player 2: Wins!!')
elif player1 == player2:
    print("It's a tie!")
else: 
    print('Something went wrong')
