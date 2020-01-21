from random import randint

exit_command = None
cpu_score = 0
player_score = 0


def play_game():
    global cpu_score, player_score
    cpu_move = ''
    player_move = input('Please choose rock, paper, or scissors: ')
    if player_move != 'rock' and player_move != 'paper' and player_move != 'scissors':
        print('Please choose a valid option.')
        play_game()
        return

    cpu_rand = randint(1, 3)
    if cpu_rand == 1:
        cpu_move = 'rock'
    elif cpu_rand == 2:
        cpu_move = 'paper'
    elif cpu_rand == 3:
        cpu_move = 'scissors'

    if player_move == cpu_move:
        print('It\'s a tie.')
    elif (player_move == 'rock' and cpu_move == 'paper') or (player_move == 'paper' and cpu_move == 'scissors') or (
            player_move == 'scissors' and cpu_move == 'rock'):
        print('You lose. You chose {} and CPU chose {}'.format(player_move, cpu_move))
        cpu_score += 1
    else:
        print('You win. You chose {} and CPU chose {}.'.format(player_move, cpu_move))
        player_score += 1
    print('CPU: {}, Player: {}'.format(cpu_score, player_score))


def start_command():
    global exit_command
    command = input('Play game? y/n: ')
    if command != 'y' and command != 'n':
        print('Please enter a valid command.')
        start_command()
        return
    elif command == 'n':
        exit_command = True
    else:
        play_game()


while not exit_command:
    start_command()