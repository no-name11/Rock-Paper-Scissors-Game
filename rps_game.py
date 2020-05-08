import random

print("welciome"'\n''this is a rock paper scissors game.')
com_score = 0
player_score = 0
played = False

def game(player_choice):
    global com_score
    global player_score
    global played
    choice = ['ROCK', 'PAPER', 'SCISSORS']
    com_choice = random.choice(choice)
    #player_choice = str(input("PLEASE SELECT YOUR WEAPON:- \n R for 'ROCK'\n P for 'PAPER'\n S for 'SCISSORS \n make your choice:-  "))

    if player_choice.upper() == "R":
        print('the computer have chosen:- ' + com_choice)
        if com_choice == "ROCK":
            print('its a draw better luck next time')
        elif com_choice == 'PAPER':
            print('computer wins \n computer gained 1 point \n better luck next time')
            com_score = com_score + 1
        elif com_choice == 'SCISSORS':
            print('you win \n you gained 1 pont..')
            player_score = player_score + 1
        played = True

    elif player_choice.upper() == "P":
        print('the computer have chosen:- ' + com_choice)
        if com_choice == "ROCK":
            print('you win \n you gained one point')
            player_score = player_score + 1
        elif com_choice == 'PAPER':
            print('its a draw better luck next timer')
        elif com_choice == 'SCISSORS':
            print('computer wins\n computer gained one piont \n better luck next time..')
            com_score = com_score + 1
        played = True

    elif player_choice.upper() == "S":
        print('the computer have chosen:- ' + com_choice)
        if com_choice == "ROCK":
            print('computer wins\n computer gained one piont \n better luck next time..')
            com_score = com_score + 1
        elif com_choice == 'PAPER':
            print('you win \n you gained one point')
            player_score = player_score + 1
        elif com_choice == 'SCISSORS':
            print('its a draw better luck next timer')
        played = True

    elif player_choice.upper() != 'R' or 'P' or 'S':
        print('select one of the given weapon and you are a DUMB...')
        played = False

    print("player score is = " + str(player_score))
    print("computer score is = " + str(com_score) + '\n\n\n')

def score(played):
    global win

    if played == True:
        if com_score != 5 and player_score != 5:
            win = False

        elif com_score == 5:
            print('computer won this series')
            win = True
            #fjhkl;
        elif player_score == 5:
            print('the player won this series(you**)')
            win = True

win = False

a = str(input('do you want to play? (y/n)'))



if a.lower() == 'y':
    play = True
    while play:
            player_choice = str(input("PLEASE SELECT YOUR WEAPON:- \n R for 'ROCK'\n P for 'PAPER'\n S for 'SCISSORS \n make your choice:-  "))
            game(player_choice)
            score(played)
            if win == True:
                play = False
                again = str(input('do you want to play another round? (y/n)'))
                if again.lower() == 'y':
                    win = False
                    com_score = 0
                    player_score = 0
                elif again.lower() == 'n':
                    print('\nsee you later \nit was nice playing with you')
                else:
                    print('\nyou really are dumb\n see you later dumbass')
            else:
                play = True
elif a.lower() == 'n':
    print('it was nice seeing you\nsee you later')
else:
    print('you are really dumb.....\n start again and enter y or n')



#game()