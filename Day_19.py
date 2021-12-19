from itertools import combinations
import numpy as np
from copy import deepcopy

scanner_number = -1
coordinates = []
with open('input.txt', 'r') as f:
    for line in f:
        if line.strip() == '':
            continue
        if line[:3] == '---':
            scanner_number += 1
            coordinates.append([])
            continue
        coords = np.asarray([int(x) for x in line.strip().split(',')])
        coordinates[scanner_number].append(coords)

#Part1
def calc_dist(coords):
    dists = {}
    for c1, c2 in combinations(coords,2):
        dist = np.linalg.norm(c1-c2)
        dists[(tuple(c1), tuple(c2))] = dist
    return dists
        
def get_overlap(dic1, dic2):
    overlap = []
    b1 = set()
    for key in dic1:
        b1.add(key[0])
        b1.add(key[1])
    for b in b1: 
        temp = set()
        for key, val in dic1.items():
            if not b in key:
                continue
            if val in dic2.values():
                for key2 in [k2 for k2, v2 in dic2.items() if v2 == val]:
                    temp2 = set((key2[0], key2[1]))
                    if temp == set():
                        temp.add(key2[0])
                        temp.add(key2[1])
                    else:
                        temp = temp.intersection(temp2)
        if temp == set():
            continue
        overlap.append([b, next(iter(temp))])
    return overlap
 
def transform(coords, ol):
    shift1 = np.asanyarray(ol[0][0])
    shift2 = np.asanyarray(ol[0][1])
    b1s, b2s = [], []
    for c in ol:
        b1s.append(np.asarray(c[0]) - shift1)
        b2s.append(np.asarray(c[1]) - shift2)
        
    for coord in coords:
        coord -= shift2
        
    if not np.all([abs(b1[0]) == abs(b2[0]) for b1, b2 in zip(b1s, b2s)]):
        if np.all([abs(b1[0]) == abs(b2[1]) for b1, b2 in zip(b1s, b2s)]):
            for b2 in b2s:
                b2[0], b2[1] = b2[1], b2[0] 
            for coord in coords:
                coord[0], coord[1] = coord[1], coord[0] 
        else:
            for b2 in b2s:
                b2[0], b2[2] = b2[2], b2[0] 
            for coord in coords:
                coord[0], coord[2] = coord[2], coord[0] 
                
    if not np.all([abs(b1[1]) == abs(b2[1]) for b1, b2 in zip(b1s, b2s)]):
        for b2 in b2s:
            b2[1], b2[2] = b2[2], b2[1]
        for coord in coords:
            coord[1], coord[2] = coord[2], coord[1] 
    
    if b1s[1][0] == -1*b2s[1][0]:
        for b2 in b2s:
            b2[0] *= -1
        for coord in coords:
            coord[0] *= -1
            
    if b1s[1][1] == -1*b2s[1][1]:
        for b2 in b2s:
            b2[1] *= -1
        for coord in coords:
            coord[1] *= -1
            
    if b1s[1][2] == -1*b2s[1][2]:
        for b2 in b2s:
            b2[2] *= -1
        for coord in coords:
            coord[2] *= -1
        
    for b2 in b2s:
        b2 += shift1
    for coord in coords:
            coord += shift1
    return
  
dists = []
for sn in range(scanner_number+1):
    dists.append(calc_dist(coordinates[sn]))

beacon_map = deepcopy(coordinates[0])  
scanner_map = [np.asarray([0,0,0])]
fused = [0]*len(coordinates)
fused[0] = 1

while not np.all(fused):
    for i in range(len(fused)):
        if fused[i]:
            for j in range(len(fused)):
                if fused[j]:
                    continue
                ol = get_overlap(dists[i], dists[j])
                if len(ol) > 11:
                    transform(coordinates[j], ol)
                    scanner_pos = [np.asarray([0,0,0])]
                    transform(scanner_pos, ol)
                    dists[j] = calc_dist(coordinates[j])
                    for c in coordinates[j]:
                        if not list(c) in [list(b) for b in beacon_map]:
                            beacon_map.append(c)
                    scanner_map.append(scanner_pos[0])
                    fused[j] = 1

print(len(beacon_map))

#Part 2
max_dist = 0
for s1, s2 in combinations(scanner_map, 2):
    dist = abs((s2-s1)[0]) + abs((s2-s1)[1]) + abs((s2-s1)[2])
    if dist > max_dist:
        max_dist = dist
        
print(max_dist)   
