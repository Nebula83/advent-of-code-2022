import os
import sys


def calc_score(outcome, rps):
    score = 0

    if outcome == 1: # win
        score += 6
    elif outcome == 0: # draw
        score += 3
    elif outcome == -1: # loose
        score += 0

    if rps == 0: # rock
        score += 1
    elif rps == 1: # paper
        score += 2
    elif rps == 2: # scissors
        score += 3
    
    return score


def get_move(opponent, outcome):
    # A: Rock
    # B: Paper
    # C: Scissors

    # X: Lose
    # Y: Draw
    # X: Win
    
    if outcome == 'X':
        if opponent == 'A': return 2
        if opponent == 'B': return 0
        if opponent == 'C': return 1
    elif outcome == 'Y':
        if opponent == 'A': return 0
        if opponent == 'B': return 1
        if opponent == 'C': return 2
    elif outcome == 'Z':
        if opponent == 'A': return 1
        if opponent == 'B': return 2
        if opponent == 'C': return 0


def run_game(opponent, player):
    outcome = -1

    # ties
    if (opponent == 'A') and (player == 0):
        outcome = 0
    elif (opponent == 'B') and (player == 1):
        outcome = 0
    elif (opponent == 'C') and (player == 2):
        outcome = 0
    # wins
    elif (opponent == 'A') and (player == 1):
        outcome = 1
    elif (opponent == 'B') and (player == 2):
        outcome = 1
    elif (opponent == 'C') and (player == 0):
        outcome = 1
    
    return outcome


def main(dirname):
    # get all raw lines
    with open(os.path.join(dirname, 'data'), 'r') as file:
        data = file.readlines()
    
    score = 0
    for game in data:
        opponent, _, outcome = game.strip().rpartition(' ')

        move = get_move(opponent, outcome)
        outcome = run_game(opponent, move)
        score += calc_score(outcome, move)

    print(f'Match outcome: {score}')    


if __name__ == '__main__':
    main(os.path.dirname(sys.argv[0]))
    