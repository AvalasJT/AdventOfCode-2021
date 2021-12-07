import numpy as np
from itertools import accumulate

f = open("input.txt", "r")
pos = [int(x) for x in f.readline().strip('\n').split(',')]

#Part 1
p = []
mp = max(pos)
for i in range(mp+1):
    p.append(pos.count(i))
    
m = np.empty((0,len(p)), int)
for i in range(mp+1):
    a = abs(np.arange(-i,mp+1-i)) * p[i]
    m = np.vstack([m,a])
    
print(min(m.sum(axis=0)))

#Part 2
n = np.empty((0,len(p)), int)
b = np.array(list(accumulate(range(mp+1))))
for i in range(mp+1):
    c = np.append(np.flip(b[1:i+1]), b[0:mp+1-i]) * p[i]
    n = np.vstack([n,c])

print(min(n.sum(axis=0)))
