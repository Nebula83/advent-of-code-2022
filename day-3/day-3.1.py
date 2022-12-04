# https://adventofcode.com/2022/day/3

import os
import sys

def char_to_score(char):
    char_val = ord(char) - 65 # ascii - A
    score = 1
    if char_val > 25:
        char_val -= 32
    else:
        score += 26
    score += char_val

    return score


def doday(data):
    scores = []
    for line in data:
        middle = int(len(line)/2)
        left = set(line[0:middle])
        right = set(line[middle:])
        for match in left.intersection(right):
            scores.append(char_to_score(match))
        
    print(f'Priority: {sum(scores)}')


def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [ line.strip() for line in f.readlines() ]
    return data


def main():
    print('--- Sample ---')
    doday(read_data('sample-data'))
    print('--- Real ---')
    doday(read_data('data'))

if __name__ == '__main__':
    main()