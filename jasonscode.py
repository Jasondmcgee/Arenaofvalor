<<<<<<< HEAD
#making a grid
grid = []
for i in range(0,10):
    row = []
    grid.append(row)
    for i in range(0,10):
        row.append(0)


boi = {
    'name': 'hero',
    'class': 'player',
    'attack': 10,
    'position': [0,0]
}

slime = {
    'name': 'slime',
    'attack': 5,
    'health': 5,
    'position': [5,5]
}

def move_player():
    move = input()
    if move == 'w':
        boi['position'][0] -= 1
    elif move == 'a':
        boi['position'][1] -= 1
    elif move == 's':
        boi['position'][0] += 1
    elif move == 'd':
        boi['position'][1] += 1
    print('to end the game press x')
    if move == 'x':
        return False
    else:
        return True

def move_slime():
    if slime['position'][0] < boi['position'][0]:
        slime['position'][0] += 1

def look_at_grid():
    grid[boi['position'][0]][boi['position'][1]] = boi['name']
    for row_num in range(0, len(grid)):
        for column_num in range(0, len(grid[row_num])):
            if row_num == boi['position'][0] and column_num == boi['position'][1]:
                grid[row_num][column_num] = boi['name']
            else:
                grid[row_num][column_num] = 0
    for i in grid:
        print(i)

game = True
while game == True:
    look_at_grid()
    game = move_player()
=======
#this is my house
print('hello')
print('isisisisissi')
>>>>>>> aa4a2cc66138c8ae7a434ad867ec0ec9a746f843
