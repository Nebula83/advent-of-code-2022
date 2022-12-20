# https://adventofcode.com/2022/day/13

import os
import sys

def compare(left, right):
    # convert into list if type mismatch
    lhs = [left] if isinstance(left, int) else left
    rhs = [right] if isinstance(right, int) else right

    # zip creates an array of pairs from both lists, which makes comparing easy
    for l, r in zip(lhs, rhs):
        # recurse if there is a type mismatch
        if isinstance(l, list) or isinstance(r, list):
            comp = compare(l, r)
        else:
            # compare left to right, smaller left should result in -1
            comp = l - r

        # we got a inequality, so stop
        if comp != 0:
            return comp
    
    # all values in the list are equal, so return the difference in length
    return len(lhs) - len(rhs)


def doday(data):
    indices = []
    for index in range(len(data)):
        left, right = data[index]
        if compare(left, right) < 0:
            indices.append(index + 1)
    print(f'Sum is {sum(indices)}')

def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [list(map(eval, line.split('\n'))) for line in f.read().split('\n\n')]
    return data


def main():
    print('--- Sample ---')
    doday(read_data('sample-data'))
    print('--- Real ---')
    doday(read_data('data'))


if __name__ == '__main__':
    main()