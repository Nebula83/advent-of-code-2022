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
    list_set = set(coords)
    unique_list = (list(list_set))
    return len(unique_list)


def printpos(h, t):
    # for y in reversed(range(0, 21)):
    for y in reversed(range(0, 5)):
        # for x in (range(0, 26)):
        for x in (range(0, 6)):
            char = '.'

            if h.x == x and h.y == y:   
               char = 'H'
            else:
                for p in reversed(range(0, len(t))):
                    if t[p].x == x and t[p].y == y:   
                        char = str(p + 1)

            print(char, end='')

                
        print()
    print()


def printtail(coords):
    tails = []
    for y in range(0, 5):
        row = []
        for x in (range(0, 6)):
            row.append('.')
        tails.append(row)

    for x, y in coords:
        tails[y][x] = '#'
     
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
    coords = []
    h = Point(0, 0)
    t = Point(0, 0)

    tail = []
    printpos(h, tail)
    for _ in range(0,2):
        tail.append(Point(0, 0))

    for line in data:
        if line == '':
            break

        newpoint = Point(h.x, h.y)
        h = newpoint.copy()
        dir, _, count =  line.rpartition(' ')
        try:
            count = int(count)
        except:
            print(line)
            raise

        for _ in range(0, count):
            print(f'Move: {line}')
            prevh = h.copy()
            h = movepoint(h, dir)

            ref = h.copy()
            for ti in range(0, len(tail)):
                
                newtail = update(ref, tail[ti], dir, prevh)
                prevh = tail[ti].copy()
                ref = newtail.copy()
                tail[ti] = newtail
                coords.append((tail[ti].x, tail[ti].y))
            printpos(h, tail)

            
                

    # printtail(coords)
    print(f'Unique positions {uniquecount(coords)}')


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
