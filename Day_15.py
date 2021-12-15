import numpy as np
import timeit

cave_list = []
with open('input.txt', 'r') as f:
    for l in f:
        cave_list.append([int(x) for x in l.strip()])
#Part 1        
cave1 = np.asarray(cave_list, 'i')

def calc_risk(cave):
    risk = np.zeros(np.shape(cave), 'i')
    changed = risk.copy()
    risk[0,1], risk[1,0] = cave[0,1], cave[1,0]
    changed[0,1], changed[1,0] = 1, 1
    
    while not np.all(changed == 0):
        new_change = np.zeros(np.shape(changed), 'i')
        for p in np.argwhere(neighbours(changed) > 0):
            check(p, cave, risk, changed, new_change)
        changed = new_change.copy()
        #print(np.sum(changed))
    return risk[-1,-1]
    
def neighbours(changed):
    chng = np.zeros((np.shape(changed)[0]+2,np.shape(changed)[1]+2), 'i')
    chng[1:-1,1:-1] = changed
    return ((np.roll(chng, 1, 0) + np.roll(chng, -1, 0) + np.roll(chng,  1, 1) + np.roll(chng, -1, 1)))[1:-1, 1:-1]

def check(point, cave, risk, changed, new_change):
    x,y = point
    if x == y == 0:
        return
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        if (not x+dx in range(np.shape(risk)[0])) or (not y+dy in range(np.shape(risk)[1])):
            continue
        elif risk[x+dx,y+dy] > 0 and ((cave[x,y]+risk[x+dx, y+dy] < risk[x,y]) or (risk[x, y] == 0)):
            risk[x, y] = risk[x+dx,y+dy]+cave[x, y]
            new_change[x,y] = 1

start = timeit.default_timer()
print(calc_risk(cave1))
print('Time: ', timeit.default_timer() - start)

#Part 2
def add_cave(cave, n):
    add_cave = cave.copy()
    add_cave += n
    add_cave[add_cave > 9] -= 9 
    return add_cave
dimx, dimy = np.shape(cave1)
cave2 = np.zeros((5*dimx,5*dimy), 'i')
for x,y in [(x,y) for x in range(5) for y in range(5)]:
    cave2[x*dimx:(x+1)*dimx, y*dimy:(y+1)*dimy] = add_cave(cave1, x+y)
    
#start = timeit.default_timer()
#print(calc_risk(cave2))
#print('Time: ', timeit.default_timer() - start)
