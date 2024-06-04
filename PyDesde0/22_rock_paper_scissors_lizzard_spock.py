import random

print('=================================')
print('Rock Paper Scissors Lizzard Spock')
print('=================================')

print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')

player = int(input('Pick a number: '))
computer = random.randint(1, 5)

if player == 1:
    player_emoji = '✊'
elif player == 2:
    player_emoji = '✋'
elif player == 3:
    player_emoji = '✌️'
elif player == 4:
    player_emoji = '🦎'
else:
    player_emoji = '🖖'

if computer == 1:
    computer_emoji = '✊'
elif computer == 2:
    computer_emoji = '✋'
elif computer == 3:
    computer_emoji = '✌️'
elif computer == 4:
    computer_emoji = '🦎'
else:
    computer_emoji = '🖖'

print(f'You choose: {player_emoji}')
print(f'CPU choose: {computer_emoji}')

if player == computer:
    print('Its a tie')
elif (player == 3 and computer == 2) or (player == 2 and computer == 1) or (player == 1 and computer == 4) or (player == 4 and computer == 5) or (player == 5 and computer == 3) or (player == 3 and computer == 4) or (player == 4 and computer == 2) or (player == 2 and computer == 5) or (player == 5 and computer == 1) or (player == 1 and computer == 3):
    print('You win')
else:
    print('CPU wins')