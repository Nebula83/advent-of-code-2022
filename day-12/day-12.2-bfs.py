# https://adventofcode.com/2022/day/12

import os
from collections import deque
import sys


def char_to_score(char):
    char_val = ord(char) - ord('A') # ascii - A
    score = 1
    if char_val > 25:
        char_val -= 32
    else:
        score += 26
    score += char_val

    return score


def parse_map(data):
    map = []
    for line in data:
        row = [char_to_score(char) for char in line]
        map.append(row)    
    return map


def get_value(map, x, y):
    return map[y][x]


def find_positions(map):
    # Find start and end points
    starts = []
    end = ()
    for row in range(len(map)):
        for col in range(len(map[row])):
            value = get_value(map, col, row)

            if value == char_to_score('a'):
                starts.append((col, row))
            elif value == char_to_score('S'):
                starts.append((col, row))
                map[row][col] = 1
            elif value == char_to_score('E'):
                end = (col, row)
                map[row][col] = 27
    return starts, end


def in_bounds(map, x, y):
  return ((x >= 0) and (x < len(map[0]))) and  ((y >= 0) and (y < len(map))) 


def bfs(map, start, end):
    visited = [[False for _ in range(len(map))] for _ in range(len(map[0]))]
    visited[start[0]][start[1]] = True
    
    queue = deque()
    first_node = (start, 0)
    queue.append(first_node)

    while queue:
        point, dist = queue.popleft()
        x, y = point
        current = get_value(map, x, y)

        if x == end[0] and y == end[1]:
            return dist

        searches = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        for search in searches:
            x, y = search
            if (in_bounds(map, x, y)
                    and (( get_value(map, x, y) == current + 1) or ( get_value(map, x, y) <= current))
                    and not visited[x][y]):

                visited[x][y] = True
                queue.append((search, (dist + 1)))

    return 10000


def doday(data):
    map = parse_map(data)
    starts, end = find_positions(map)

    results = []
    for start in starts:
        x, y = start
        sv = get_value(map, x, y)
        x, y = end
        ev = get_value(map, x, y)
        shortest = bfs(map, start, end)
        results.append(shortest)
    print(min(results))


def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    print('--- Sample ---')
    doday(read_data('sample-data'))
    print('--- Real ---')
    doday(read_data('data'))


if __name__ == '__main__':
    main()