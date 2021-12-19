import ast
import numpy as np
from itertools import combinations
from copy import deepcopy

snumbers = []
with open('input_test.txt', 'r') as f:
    for line in f:
        snumbers.append(ast.literal_eval(line.strip()))
        
#Part 1
def add(n1, n2):
    return reduce([n1, n2])

def reduce(n):
    while True:
        T, l, r, n = explode(n, 0)
        if T:
            continue
        T, n = split(n)
        if T:
            continue
        break #nither explode nor split
    return n

def explode(n, layer):
    if layer == 4 and np.shape(n) != ():
        return True, n[0], n[1], 0
    
    if np.shape(n) == ():
        return False, 0, 0, n
        
    T, l, r, sub = explode(n[0], layer+1)
    if T:
        n[0] = sub
        n[1] = add_right(n[1], r)
        return T, l, 0, n
    
    T, l, r, sub = explode(n[1], layer+1)
    if T:
        n[1] = sub
        n[0] = add_left(n[0], l)
        return T, 0, r, n    
    return T, l, r, n
        
def add_right(n, r):
    if np.shape(n) == ():
        n += r
        return n
    n[0] = add_right(n[0], r)
    return n

def add_left(n, l):
    if np.shape(n) == ():
        n += l
        return n
    n[1] = add_left(n[1], l)
    return n

def split(n):
    if np.shape(n) == (): 
        if n > 9:#split
            return True, [int(n/2), round(n/2 + 0.1)]
        else:
            return False, n
        
    T, sub = split(n[0])
    if T:
        n[0] = sub
        return T, n
    
    T, sub = split(n[1])
    if T:
        n[1] = sub
        return T, n
    
    return False, n

def get_mag(n):
    if np.shape(n) == ():
        return n
    return 3*get_mag(n[0]) + 2*get_mag(n[1])

numbers = deepcopy(snumbers)
for i in range(1, len(numbers)):
    numbers[0] = add(numbers[0], numbers[i])

print(get_mag(numbers[0]))

#Part 2
max_mag = 0
for sno1, sno2 in combinations(snumbers,2):
    sn1, sn2 = deepcopy(sno1), deepcopy(sno2)
    mag = get_mag(add(sn1, sn2))
    if mag > max_mag:
        max_mag = mag
    sn1, sn2 = deepcopy(sno1), deepcopy(sno2)
    mag = get_mag(add(sn2, sn1))
    if mag > max_mag:
        max_mag = mag
print(max_mag)
