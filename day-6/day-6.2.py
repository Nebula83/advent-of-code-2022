# https://adventofcode.com/2022/day/6

import os
import sys

def doday(data):
    length = 14
    for line in data:
        # print(line)
        for window_start in range(0, len(line) - (length - 1)):

            window = line[window_start:window_start + length]
            # print(f'{window_start}: {window}')

            window_set = set(window)
            # print(window_set)
            if len(window_set) == length:
                print(window_start + length)
                break 


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