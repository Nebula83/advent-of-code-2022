import os
import sys


def calc_score(outcome, rps):
    score = 0
    
    # A: Rock
    # B: Paper
    # C: Scissors

    # X: Rock
    # Y: Paper
    # X: Scissors

    if outcome == 1: # win
        score += 6
    elif outcome == 0: # draw
        score += 3
    elif outcome == -1: # lose
        score += 0

    if rps == 'X': # rock
        score += 1
    elif rps == 'Y': # paper
        score += 2
    elif rps == 'Z': # scissors
        score += 3
    
    return score


def run_game(opponent, player):
    outcome = -1

    # ties
    if (opponent == 'A') and (player == 'X'):
        outcome = 0
    elif (opponent == 'B') and (player == 'Y'):
        outcome = 0
    elif (opponent == 'C') and (player == 'Z'):
        outcome = 0
    # wins
    elif (opponent == 'A') and (player == 'Y'):
        outcome = 1
    elif (opponent == 'B') and (player == 'Z'):
        outcome = 1
    elif (opponent == 'C') and (player == 'X'):
        outcome = 1
    
    return outcome


def main(dirname):
    # get all raw lines
    with open(os.path.join(dirname, 'data'), 'r') as file:
        data = file.readlines()
    
    score = 0
    for game in data:
        opponent, _, player = game.strip().rpartition(' ')
        outcome = run_game(opponent, player)
        score += calc_score(outcome, player)
    print(f'Match outcome: {score}')    


if __name__ == '__main__':
    main(os.path.dirname(sys.argv[0]))
    