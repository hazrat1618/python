print('Welcome to game: rock, paper and scissors!')

player1 = input('Enter your move: ')
player2 = input('Enter your move: ')

if player1 == 'Rock' and player2 == 'Scissors' or player1 == 'Scissors' and player2 == 'Rock':
    print('Player with Rock wins!')
elif player1 == 'Scissors' and player2 == 'Paper' or player1 == 'Paper' and player2 == 'Scissors':
    print('Player with Scissors wins')
elif player1 == 'Paper' and player2 == 'Rock' or player1 == 'Rock' and player2 == 'Paper':
    print('Player with Paper wins')
elif player1 == player2:
    print('It is a tie')
else:
    print('Wrong entry')

