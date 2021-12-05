# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 18:39:00 2021

@author: rist
"""
import numpy as np

f = open("input.txt", "r")
lines = f.readlines()
f.close()

#Part 1
dim = 0
x1s, y1s, x2s, y2s = [], [], [], []
        
for line in lines:
    start, end = line.strip('\n').split(' -> ')
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if max(x1, x2, y1, y2) > dim:
        dim = max(x1, x2, y1, y2)
    x1s.append(x1)
    x2s.append(x2)
    y1s.append(y1)
    y2s.append(y2)
    
ground = np.zeros((dim+1,dim+1), int)
for i in range(len(x1s)):
    if x1s[i] == x2s[i]:
        s, e = min(y1s[i],y2s[i]), max(y1s[i],y2s[i])
        ground[x1s[i], s:e+1] += 1
    elif y1s[i] == y2s[i]:
        s, e = min(x1s[i],x2s[i]), max(x1s[i],x2s[i])
        ground[s:e+1, y1s[i]] += 1
    else:
        continue #print('Not a horizontal or vertical line')
print(len(np.where(ground > 1)[0]))

#Part 2
ground = np.zeros((dim+1,dim+1), int)
for i in range(len(x1s)):
    diff = max(abs(x2s[i] - x1s[i]) ,abs(y2s[i] - y1s[i]))
    dx = int((x2s[i] - x1s[i]) / diff) 
    dy = int((y2s[i] - y1s[i]) / diff)
    
    for j in range(diff+1):
        ground[x1s[i]+j*dx][y1s[i]+j*dy] += 1
    
print(len(np.where(ground > 1)[0]))
