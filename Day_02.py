# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 18:39:00 2021

@author: rist
"""

list = []

f = open("input.txt", "r")
list = [x.split() for x in f]
f.close()

for x in list:
    x[1] = int(x[1])

#Part 1
h = 0
d =  0

for x in list:
    if x[0] == 'forward':
        h += x[1]
    elif x[0] == 'down':
        d += x[1]
    elif x[0] == 'up':
        d -= x[1]
    else:
        print('Invalid command')
        
print(h*d)

  
    
#Part 2
h = 0
d = 0
a = 0

for x in list:
    if x[0] == 'forward':
        h += x[1]
        d += a * x[1]
    elif x[0] == 'down':
        a += x[1]
    elif x[0] == 'up':
        a -= x[1]
    else:
        print('Invalid command')
        
print(h*d)