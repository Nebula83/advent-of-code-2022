# https://adventofcode.com/2022/day/9

import os
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

    def copy(self):
        return Point(self.x, self.y)


def uniquecount(coords):
    unique_list = (list(coords))
    return len(unique_list)
 

def printpos(h, t):
    for y in reversed(range(0, 5)):
        for x in (range(0, 6)):
            if h.x == x and h.y == y:   
                print('H', end='')
            elif t.x == x and t.y == y:
                print('T', end='')
            else:
                print('.', end='')
        print()
    print()


def printtail(coords):
    tails = []
    for y in range(0, 5):
        row = []
        for x in (range(0, 6)):
            row.append('.')
        tails.append(row)

    for point in coords:
        tails[point.y][point.x] = '#'
     
    for y in reversed(range(0, 5)):
        for x in (range(0, 6)):
           print(tails[y][x], end='')
        print()


def movepoint(p, dir):
    if dir == 'L':
        p.x -= 1
    elif dir == 'R':
        p.x += 1
    elif dir == 'U':
        p.y += 1
    elif dir == 'D':
        p.y -= 1

    return p


def update(h, t, dir, prevh):
    newpoint = Point(t.x, t.y)
    xdelta = abs(h.x - t.x)
    ydelta = abs(h.y - t.y)

    if not (xdelta <=1 and ydelta <= 1):
        if t.x != h.x and t.y != h.y:
            # do diagonal
            newpoint = prevh.copy()
        else:
            newpoint = movepoint(newpoint, dir)

    return newpoint


def doday(data):
    h = Point(0, 0)
    t = Point(0, 0)
    dirs = ['']
    head = [h]
    tail = [t]
    points = set()

    # Calculate head
    for line in data:
        dir, _, count =  line.rpartition(' ')
        count = int(count)
        for _ in range(0, count):
            h = h.copy()
            h = movepoint(h, dir)
            head.append(h)
            dirs.append(dir)

    # Calculate tail
    for i in range(1, len(head)):
        t = t.copy()
        if i > 1:
            prevh = head[i - 1]
        else:
            prevh = Point(0, 0)
            
        t = update(head[i], t, dirs[i], prevh)
        tail.append(t)
        points.add((t.x, t.y))

    # Plot it
    for i in range(0, len(head)):
        printpos(head[i], tail[i])
    
    print(f'Unique positions {uniquecount(points)}')

def read_data(name):
    with open(os.path.join(os.path.dirname(sys.argv[0]), name)) as f:
        data = [ line.strip() for line in f.readlines() ]
    return data


def main():
    print('--- Sample ---')
    doday(read_data('sample-data'))
    print()
    # print('--- Real ---')
    # doday(read_data('data'))

if __name__ == '__main__':
    main()
