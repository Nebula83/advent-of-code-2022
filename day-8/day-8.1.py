# https://adventofcode.com/2022/day/8

import os
import sys

def get_tree(trees, row, column):
    return trees[row][column]


def search_left(match, trees, row, column):
    for scol in range(0, column):
        tree = get_tree(trees, row, scol)
        if tree >= match:
            return True
    return False


def search_right(match, trees, row, column):
    for scol in range(column + 1, len(trees[0])):
        tree = get_tree(trees, row, scol)
        if tree >= match:
            return True
    return False


def search_top(match, trees, row, column):
    for srow in range(0, row):
        tree = get_tree(trees, srow, column)
        if tree >= match:
            return True
    return False
    

def search_bottom(match, trees, row, column):
    for srow in range(row + 1, len(trees)):
        tree = get_tree(trees, srow, column)
        if tree >= match:
            return True
    return False


def doday(data):
    trees = []
    for line in data:
        tree_row = [int(tree) for tree in list(line)]
        trees.append(tree_row)

    # Borders
    visible = (len(trees) * 2) + 2 * (len(trees[0]) - 2)

    for row in range(1, len(trees)-1):
        for col in range(1, len(trees[row])-1):
            tree = get_tree(trees, row, col)
            
            top_safe = search_top(tree, trees, row, col)
            if not top_safe:
                visible += 1
                continue

            bottom_safe = search_bottom(tree, trees, row, col)
            if not bottom_safe:
                visible += 1
                continue

            left_safe = search_left(tree, trees, row, col)
            if not left_safe:
                visible += 1
                continue

            right_safe = search_right(tree, trees, row, col)
            if not right_safe:
                visible += 1
                continue

    print(f'Visible trees {visible}')


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