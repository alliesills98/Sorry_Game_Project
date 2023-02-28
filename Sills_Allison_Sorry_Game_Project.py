
import random

players = 0
player_score = []
player_name = []
score = 0
#create a while loop so the game is replayable
while True:
    print("This game can be played with 2-4 players. Enter the number of players: ")
    num_players = int(input())
    #validate number of players
    while num_players < 2 or num_players > 4:
        print("Invalid number of players! Enter a valid number of players: ")
        num_players = int(input())
        #this will help set score and roll conditions 
    if num_players == 2:
        player_score = [0,0]
    if num_players == 3:
        player_score = [0,0,0]
    if num_players == 4:
        player_score = [0,0,0,0]
        # get player names
    for i in range(num_players):
        name = input("Enter player name: ")
        player_name.append(name)
    while True:
        #create a while loop for player turns
        for i in range(len(player_score)):
            roll = random.randint(2,12)
            if roll == 2:
                player_score[i] += 2
            if roll == 3:
                player_score[i] +=2
            if roll == 4:
                player_score[i] -= 1
            if roll == 5:
                player_score[i] -= 2
            if roll == 6:
                player_score[i] +=6
            if roll == 7:
                player_score[i] += 7
            if roll ==8:
                player_score[i] += 0
            if roll == 9:
                player_score[i] += 9
            if roll == 10:
                player_score[i] += 10
            if roll == 11:
                player_score[i] -= 11
            if roll == 12:
                player_score[i] = 0
            if player_score[i] > 50:
                player_score[i] -= roll
            if player_score[i] == 50:
                print(str(player_name[i]) + " Congratualations you win!!!!")
                break
        if player_score[i] == 50:
            break
        else:
            print(str(player_name[i]) + " your score is " + str(player_score[i])) 

    print("Would you like to play again? Y or N: ")
    if input() == "N" or input()== 'n':
        break
    



