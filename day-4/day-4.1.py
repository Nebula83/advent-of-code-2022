# https://adventofcode.com/2022/day/X

import os
import sys

def isoverlapping(range1, range2):
    len1 = len(range1)
    len2 = len(range2)

    return (len(range1.intersection(range2)) == len1) or \
        (len(range2.intersection(range1)) == len2)


def rangetorange(r):
    start, _, end = r.rpartition('-')
    return set(range(int(start), int(end) + 1))


def doday(data):
    overlaps = 0
    for line in data:
        range1, _, range2 = line.rpartition(',')
        range1 = rangetorange(range1)
        range2 = rangetorange(range2)

        if (isoverlapping(range1, range2)):
            overlaps += 1

    print(f'Sections that fully overlap are {overlaps}')


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