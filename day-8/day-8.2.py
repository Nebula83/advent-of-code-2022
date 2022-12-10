# https://adventofcode.com/2022/day/8

import os
import sys

def get_tree(trees, row, column):
    return trees[row][column]


def search_left(match, trees, row, column):
    count = 0
    for scol in reversed(range(0, column)):
        tree = get_tree(trees, row, scol)
        count += 1
        if tree >= match:
            break
    return count


def search_right(match, trees, row, column):
    count = 0
    for scol in range(column + 1, len(trees[0])):
        tree = get_tree(trees, row, scol)
        count += 1
        if tree >= match:
            break
    return count


def search_top(match, trees, row, column):
    count = 0
    for srow in reversed(range(0, row)):
        tree = get_tree(trees, srow, column)
        count += 1
        if tree >= match:
            break
    return count
    

def search_bottom(match, trees, row, column):
    count = 0
    for srow in range(row + 1, len(trees)):
        tree = get_tree(trees, srow, column)
        count += 1
        if tree >= match:
            break
    return count


def doday(data):
    trees = []
    for line in data:
        tree_row = [int(tree) for tree in list(line)]
        trees.append(tree_row)

    scores = []
    for row in range(1, len(trees)-1):
        for col in range(1, len(trees[row])-1):
            tree = get_tree(trees, row, col)
            
            tcount = search_top(tree, trees, row, col)
            bcount = search_bottom(tree, trees, row, col)
            lcount = search_left(tree, trees, row, col)
            rcount = search_right(tree, trees, row, col)

            scores.append(tcount * bcount * lcount * rcount)
    
    print(f'Max score {max(scores)}')


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