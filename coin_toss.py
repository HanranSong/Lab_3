"""
-------------------------------------------------------------------------------
Coin Toss Game
In the coin toss game, user choose one side of a coin "head or tail." Then,
two computer player will toss the coin. If computer player's result equal to
user's choice, they will win. There are four tries in one round, after each
round, the program will providing feedback about which player won the whole
round of the game. Finally, the program will ask user whether they want to
play another round.
-------------------------------------------------------------------------------
"""

import random


def main():
    # read the file "instructions.txt" and print it at the beginning of the
    # program
    instructions_file = open('instructions.txt', 'r')
    instructions = instructions_file.read()
    instructions_file.close()
    print(instructions)
    
    # the counters for the final summary statistics
    ties = 0
    player_one_wins = 0
    player_two_wins = 0

    # Set the condition key as "True" in the beginning. If user don't want
    # to play it again at the end of the program, set it to "False" and stop
    # the whole while loop.
    key = True
    while key:
        player_one_points = 0  # counter for player 1's round points
        player_two_points = 0  # counter for player 2's round points
    
        player_one_tossed = [0, 0, 0, 0]  # player 1's results' sequence
        player_two_tossed = [0, 0, 0, 0]  # player 2's results' sequence
    
        time_one = 0  # how many times "H H" shows in the sequence 1
        time_two = 0  # how many times "H H" shows in the sequence 2
    
        # four tries in a round
        for i in range(4):
            user_decision = input('Heads or Tails ? Type H or T >')  #
            # collect user's decision
            answer = ['H', 'T']  # the all two possible solutions for coin
            # tossing
    
            # randomly generate computer players' results
            player_one = answer[random.randint(0, 1)]
            player_one_tossed[i] = player_one
            player_two = answer[random.randint(0, 1)]
            player_two_tossed[i] = player_two
    
            # show players' toss results
            print('Player 1 has tossed', player_one)
            print('Player 2 has tossed', player_two)
    
            # compare players' results with the answer and tell whether it's
            # correct. If result correct, add one point to the according player
            if player_one == user_decision:
                print('Player 1 wins')
                player_one_points += 1
            if player_two == user_decision:
                print('Player 2 wins')
                player_two_points += 1
    
        # show the round statistics
        # add one win for the winner, if it's tie, add one tie
        print('ROUND STATS')
        if player_one_points > player_two_points:
            print('Player 1 wins this round')
            player_one_wins += 1
        elif player_two_points > player_one_points:
            print('Player 2 wins this round')
            player_two_wins += 1
        else:
            print('It is a tie')
            ties += 1
    
        # points
        print('Player 1 points', player_one_points)
        print('Player 2 points', player_two_points)
    
        # sequences
        print('Player 1 tossed', player_one_tossed)
        print('Player 2 tossed', player_two_tossed)
    
        # count how many "H H" shows in the sequence
        for i in range(3):
            if player_one_tossed[i] == 'H' and player_one_tossed[i + 1] == 'H':
                time_one += 1
        for i in range(3):
            if player_two_tossed[i] == 'H' and player_two_tossed[i + 1] == 'H':
                time_two += 1
        print('H H found in the player 1 sequence ' + str(time_one) + ' times')
        print('H H found in the player 2 sequence ' + str(time_two) + ' times')

        # ask user whether they want to play it another round when they
        # don't want to play for another round, show the final summary
        # statistics.
        again = input('Do you want to play another round? y/n >')
        # when user input "n", change key to "False" and stop the while loop
        if again.lower() != 'y':
            key = False
            print('SUMMARY STATS')
            print('number of ties', ties)
            print('number of player 1 wins', player_one_wins)
            print('number of player 2 wins', player_two_wins)


main()
