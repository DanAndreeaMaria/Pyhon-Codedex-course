import random

player = 0
computer = 0

print('==============================================')
print('✨ Hello and welcome to RPS game! Have fun!✨')
print('==============================================')
print('**********************************************')
print('\n')
print('🟣 1 is for “✊” (Rock).')
print('🟡 2 is for “✋” (Paper).')
print('🟠 3 is for “✌” (Scissors).')
print('🟢 4 is for “🦎” (Lizard).')
print('🔴 5 is for “🖖” (Spock).')
print('\n')
print('**********************************************')
print('Scissors cut Paper.')
print('Paper covers Rock.')
print('Rock crushes Lizard.')
print('Lizard poisons Spock.')
print('Spock smashes Scissors.')
print('Scissors beat Lizard.')
print('Lizard eats Paper.')
print('Paper disproves Spock.')
print('Spock vaporizes Rock.')
print('Rock breaks Scissors.')
print('**********************************************')
print('\n')
print('----------------------------------------------')

name = input('Enter your name please: ')
player = int(input('Select a number between 1 and 5: '))
print('\n')
if player == 1:
    print('You chose ✊')
elif player == 2:
    print('You chose ✋')
elif player == 3:
    print('You chose ✌')
elif player == 4:
    print('You chose 🦎')
elif player == 5:
    print('You chose 🖖')

computer = random.randint(1, 5)
if computer == 1:
    print('Computer chose ✊')
elif computer == 2:
    print('Computer chose ✋')
elif computer == 3:
    print('Computer chose ✌')
elif computer == 4:
    print('Computer chose 🦎')
elif computer == 5:
    print('Computer chose 🖖')

print('\n')

if player == computer:
    print('It\'s a tie!')
elif player == 1 and computer == 2:
    print('Computer wins!')
elif player == 1 and computer == 3:
    print(f'{name} wins!')
elif player == 1 and computer == 4:
    print(f'{name} wins!')
elif player == 1 and computer == 5:
    print('Computer wins!')
elif player == 2 and computer == 3:
    print('Computer wins!')
elif player == 2 and computer == 4:
    print('Computer wins!')
elif player == 2 and computer == 5:
    print(f'{name} wins!')
elif player == 3 and computer == 1:
    print(f'{name} wins!')
elif player == 3 and computer == 2:
    print(f'{name} wins')
elif player == 3 and computer == 4:
    print(f'{name} wins!')
elif player == 3 and computer == 5:
    print('Computer wins!')
elif player == 4 and computer == 1:
    print('Computer wins!')
elif player == 4 and computer == 2:
    print(f'{name} wins!')
elif player == 4 and computer == 3:
    print('Computer wins!')
elif player == 4 and computer == 5:
    print(f'{name} wins!')
elif player == 5 and computer == 1:
    print(f'{name} wins!')
elif player == 5 and computer == 2:
    print('Computer wins!')
elif player == 5 and computer == 3:
    print(f'{name} wins!')
elif player == 5 and computer == 4:
    print('Computer wins!')
else:
    print("Wrong input!")


























