import numpy as np

with open("input.txt", 'r') as file:
    data = [[c for c in x] for x in file.read().split('\n') if x != '']
floor = np.asarray(data)
floorT, move = np.zeros(np.shape(floor), 'str'), np.zeros(np.shape(floor), 'i')
steps = 0

#Part 1
while not np.all(floor == floorT):
    steps += 1
    floorT[:] = floor[:]
    move[:,:] = 0
    move[np.logical_and(floor == '>', np.roll(floor, -1, 1) == '.')] = 1
    floor[move == 1] = '.'
    floor[np.roll(move, 1, 1) == 1] = '>'
    move[:,:] = 0
    move[np.logical_and(floor == 'v', np.roll(floor, -1, 0) == '.')] = 1
    floor[move == 1] = '.'
    floor[np.roll(move, 1, 0) == 1] = 'v'   
print(steps)
