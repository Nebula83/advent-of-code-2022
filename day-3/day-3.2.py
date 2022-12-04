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
    for index in range(0, len(data), 3):
        badge = data[index].intersection(data[index + 1], data[index + 2])
        scores.append(char_to_score(badge.pop()))
        
    print(f'Priority: {sum(scores)}')


def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [ set(line.strip()) for line in f.readlines() ]
    return data


def main():
    print('--- Sample ---')
    doday(read_data('sample-data'))
    print('--- Real ---')
    doday(read_data('data'))

if __name__ == '__main__':
    main()