def main():
    # get all raw lines
    with open('data', 'r') as file:
        data = file.read()
    elves = data.split('\n\n')
    
    calories = []
    for elve in elves: 
        calories.append(sum([int(food) for food in elve.split('\n')]))
    
    calories.sort(reverse=True)
    print(f'The sum of the top three elve carrying the most calories {sum([calories[index] for index in range(0, 3)])}')


if __name__ == '__main__':
    main()