# https://adventofcode.com/2022/day/6

import os
import sys

def doday(data):
    for line in data:
        print(line)
        for window_start in range(0, len(line) - 3):

            window = line[window_start:window_start + 4]
            # print(f'{window_start}: {window}')

            window_set = set(window)
            # print(window_set)
            if len(window_set) == 4:
                print(window_start + 4)
                break 
            # print()
        # break



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