from random import randint

def intro():
    print('Welcome to the hottest new game craze, Guess! That! Number!')
    print('What\'s your name contestant?')

    input()

    print('AH that\'s a lovely name! Truly breath taking!')
    print('A random number between 1 and 10 has been generated using our special rng technology. It\'s your job to Guess! That! Number!')
    print('You have three tries to guess the number!')
    print('Please type your first guess below!')



program_running = True

while program_running == True:

    intro()

    game_running = True

    while game_running == True:

        number_true = randint(1, 10)

        round_running = True

        counter = 0

        while round_running == True:
            guess_one = int(input())

            if guess_one == number_true:
                print('You won')
                print('Would you like to play again? Yes or No?')
                play_again = str(input())
                if play_again == 'yes':
                    game_running = False
                    round_running = False
                    #this might be wrong
                else:
                    print('See you next time')
                    game_running = False
                    round_running = False
                    program_running = False

            elif guess_one > int(number_true):
                print('Sorry too high')
                counter += 1

            elif guess_one < int(number_true):
                print('Sorry too low')
                counter += 1
            
            if counter >= 3:
                print('That\'s your last guess. Would you like to play again? Yes or No?')
                ye = str(input())
                if ye == 'yes':
                    game_running = False
                    round_running = False
                    # this might be wrong
                else:
                    print('See you next time')
                    game_running = False
                    round_running = False
                    program_running = False
