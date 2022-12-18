# https://adventofcode.com/2022/day/11

import os
import re
import sys

class Monkey:
    def __init__(self):
        self.id = 0
        self.items = []
        self.op = ()
        self.test = ()
        self.truetarget = 0
        self.falsetarget = 0
        self.inspected = 0
    
    
    def __repr__(self):
        monkey = ''
        monkey += ('---------------------------------------\n')
        monkey += (f'Id:        {self.id}\n')
        monkey += (f'Items:     {self.items}\n')
        monkey += (f'Operation: {self.op}\n')
        monkey += (f'Test:      {self.test}\n')
        monkey += (f'True:      {self.truetarget}\n')
        monkey += (f'False:     {self.falsetarget}\n')
        monkey += (f'Inspected: {self.inspected}\n')
        monkey += ('---------------------------------------\n')
        
        return monkey

def GGD(a, b):
    if b == 0:
        return b
    return GGD(b, b % a)

def doday(data):
    # Parse
    monkeys = []
    for line in data:
        if line.startswith('Monkey'):
            monkeys.append(Monkey())
            monkeys[-1].id = int(line[7])
        elif line.startswith('Starting items:'):
            monkeys[-1].items = eval(f'[{line[16:]}]')
        elif line.startswith('Operation:'):
            monkeys[-1].op = line[17:]
            monkeys[-1].op = eval(f'lambda old :{monkeys[-1].op}')
        elif line.startswith('Test:'):
            monkeys[-1].test = int(line[19:])
        elif line.startswith('If true:'):
            monkeys[-1].truetarget = int(line[24:])
        elif line.startswith('If false:'):
            monkeys[-1].falsetarget = int(line[25:])

    lcm = 1
    for monkey in monkeys:
        lcm *= monkey.test
    print(f'Using LMC of {lcm}')

    for round in range(0, 10000):
        for monkey in  monkeys:
            # print (f'  Monkey  {monkey.id}')
            for item in monkey.items:
                # print (f'    Monkey inspects an item with a worry level of {item}.')
                monkey.inspected += 1
                worry = monkey.op(item)
                # print (f'      Worry level is {worry}.')
                # worry = worry // 3
                worry %= lcm
                # print (f'      Monkey gets bored with item. Worry level is divided by 3 to {worry}.')
                if (worry % monkey.test) == 0:
                    # print (f'      Current worry level is divisible by {monkey.test}.')
                    # print (f'      Item with worry level {worry} is thrown to monkey {monkey.truetarget}.')
                    monkeys[monkey.truetarget].items.append(worry)
                else:
                    # print (f'      Current worry level is not divisible by {monkey.test}.')
                    # print (f'      Item with worry level {worry} is thrown to monkey {monkey.falsetarget}.')
                    monkeys[monkey.falsetarget].items.append(worry)
            # Clear queue
            monkey.items = []

    print()
    print('-- Items --')
    for monkey in  monkeys:
        print(f'Monkey {monkey.id}: {monkey.items}')
    
    print()
    print('-- Inspections --')
    inspects = []
    for monkey in  monkeys:
        inspects.append(monkey.inspected)
        print(f'Monkey {monkey.id}: inspected {monkey.inspected} items.')
    inspects.sort()

    print(f'Scores: {inspects[-2] * inspects[-1]}')


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
