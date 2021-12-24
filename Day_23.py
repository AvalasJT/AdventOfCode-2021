import numpy as np
from copy import deepcopy

#Part 1
map1 = np.asarray(['.']*33).reshape((3,11))
map1[1:3, 0:2] = map1[1:3,-2:] = map1[1:3,3] = map1[1:3,5] = map1[1:3,7]= '#'
map1[2,4] = map1[1,8] = 'A'
map1[1,2] = map1[1,4] = 'B'
map1[2,2] = map1[2,8] = 'C'
map1[1,6] = map1[2,6] = 'D'

#Part 2
map2 = np.asarray(['.']*55).reshape((5,11))
map2[1:5, 0:2] = map2[1:5,-2:] = map2[1:5,3] = map2[1:5,5] = map2[1:5,7]= '#'
map2[4,4] = map2[1,8] = map2[3,6] = map2[2,8] = 'A'
map2[1,2] = map2[1,4] = map2[3,4] = map2[2,6] = 'B'
map2[4,2] = map2[4,8] = map2[2,4] = map2[3,8] = 'C'
map2[1,6] = map2[4,6] = map2[2,2] = map2[3,2] = 'D'

room = {'A':2, 'B':4, 'C':6, 'D':8}
roomT = {2:'A', 4:'B', 6:'C', 8:'D'}

def get_possible_moves(map):
    moves = can_direct_change(map) #if amphi can go directly into right room -> always do that first
    if moves != []:
        return moves
    dim = np.shape(map)[0]
    for i in range(11): #hallway
        c = map[0][i]
        if c == '.':
            continue
        else: #is amphi
            if i < room[c]:
                if np.any(map[0][i+1:room[c]+1] != '.'): #way is blocked
                    continue
            elif i > room[c]:
                if np.any(map[0][room[c]:i] != '.'):
                    continue
            
            if not np.all([(map[j][room[c]] == '.') or (map[j][room[c]] == c) for j in range(1,dim)]): #room is blocked
                continue
            
            for j in range(dim-1,0, -1):  #if you amphi can enter room -> always do that
                if map[j][room[c]] == '.':
                    moves.append([(0,i), (j,room[c])])
                    return moves
    
    for i in [2, 4, 6, 8]: #rooms
        if np.all([(map[j][i] == '.') or (map[j][i] == roomT[i]) for j in range(1,dim)]): #don't leave good rooms
            continue
        for j in range(1,dim):
            c = map[j][i]
            if c == '.': #get first amphi
                continue
            else:
                for k in range(i):
                    if k in roomT: #don't stop in front of door
                        continue
                    if np.all(map[0][k:i] == '.'): #check if way is free
                        moves.append([(j,i), (0,k)]) #add move
                for l in range(i+1,11): #other side
                    if l in roomT:
                        continue
                    if np.all(map[0][i:l+1] == '.'):
                        moves.append([(j,i), (0,l)])
            break #only first amphi can leave the room
                        
    return moves

def do_move(map, move):
    m = deepcopy(map)
    m[move[1]] = m[move[0]]
    m[move[0]] = '.'
    return m
 
def solve(map, seq, solutions, cost):
    global best_cost
    m = deepcopy(map)
    if is_solved(m):
        solutions.append(seq)
        best_cost = cost
        print('Found a new/better solution! Try: ', best_cost)
        return
    if is_blocked(m):
        return
    
    moves = get_possible_moves(m)
    if len(moves) == 1:
        new_cost = calc_cost(m, moves[0])
        if cost + new_cost >= best_cost:
            return
        solve(do_move(m, moves[0]), seq + [moves[0]], solutions, cost+new_cost)
        return
        
    for i, move in enumerate(moves):
        if len(seq) < 2: #just for estimating remaining time
            print(len(seq), i, 'of', len(moves)-1)
        new_cost = calc_cost(m, move)
        if cost + new_cost >= best_cost:
            continue
        solve(do_move(m, move), seq + [move], solutions, cost+new_cost)

def is_solved(m):
    if not np.all(m[0][:] == '.'):
        return False
    for C,i in room.items():
        if not np.all(m[1:,i] == C):
            return False
    return True
       
def calc_cost(m, move):
    costs = {'A':1, 'B':10, 'C':100, 'D':1000}
    c = costs[m[move[0]]]
    if move[0][0] == 0 or move[1][0] == 0:
        steps = abs(move[1][0]-move[0][0]) + abs(move[1][1]-move[0][1])
    else:
        steps = abs(move[1][1]-move[0][1]) + move[0][0] + move[1][0]
    return c*steps

def num_solved(m):
    n = 0
    dim = np.shape(m)[0]
    for C,i in room.items():
        if np.all([(m[j][i] == '.') or (m[j][i] == roomT[i]) for j in range(1,dim)]):
            n += len(np.argwhere(m[1:,i] == roomT[i]))
    return n

def num_in_hallway(m):
    return len(np.argwhere(m[0,:] != '.'))

def is_blocked(m):
    for i in range(np.shape(m)[1]-1):
        a = m[0,i]
        if a == '.':
            continue
        for j in range(i+1, np.shape(m)[1]):
            b = m[0,j]
            if b == '.':
                continue
            if room[a] >= j and room[b] <= i:
                return True
            
    dim = np.shape(m)[0] 
    for C, i in room.items():
        if m[0][i] == C and not np.all([(m[j][i] == '.') or (m[j][i] == C) for j in range(1,dim)]):
            return True
    return False

def can_direct_change(m):
    dim = np.shape(m)[0]
    for C,i in room.items():
        if m[1,i] != '.':
            continue
        if np.all([(m[j][i] == '.') or (m[j][i] == roomT[i]) for j in range(2,dim)]):
            pos = 0
            for p in range(dim-1,0, -1):
                if m[p,i] == '.':
                    pos = p
                    break
                    
            for D,j in room.items():
                if i == j:
                    continue
                if not np.all([m[0][x] == '.' for x in range(min([i,j]), max([i,j])+1)]):
                    continue
                for k in range(1,dim):
                    if m[k,j] == '.':
                        continue
                    if m[k,j] != roomT[i]: #if not then somebody in j who can enter room i
                        break 
                    return [[(k, j), (pos,i)]]
    return []

#Part 1        
best_cost = 10**8   
solutions1 = []
solve(map1, [], solutions1, 0) 
print('Final sulution: ', best_cost)

#Part 2
best_cost = 10**8
solutions2 = []
solve(map2, [], solutions2, 0) 
print('Final sulution: ', best_cost)
