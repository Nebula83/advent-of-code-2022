# https://adventofcode.com/2022/day/13

import functools
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
    # add dividers
    data.append([[2]])
    data.append([[6]])

    # sort the data
    data.sort(key=functools.cmp_to_key(compare))
    
    indices = []
    for index in range(len(data)):
        if data[index] == [[2]] or data[index] == [[6]]:
            indices.append(index + 1)
    print(f'Key is {functools.reduce(lambda lhs, rhs: lhs * rhs, indices)}')
    

def read_data(name):

    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [eval(line.strip()) for line in f.readlines() if line != '\n']
    return data


def main():
    print('--- Sample ---')
    doday(read_data('sample-data'))
    print('--- Real ---')
    doday(read_data('data'))


if __name__ == '__main__':
    main()