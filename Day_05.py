import numpy as np

f = open("input.txt", "r")
lines = f.readlines()
f.close()

#Part 1
ground = np.zeros((1,1), int)

for line in lines:
    x1, y1, x2, y2 = [int(x) for x in (line.strip('\n').split(' -> ')[0]+','+line.strip('\n').split(' -> ')[1]).split(',')]
    while max(x1, x2, y1, y2) > np.shape(ground)[0] - 1:
        ground = np.append(ground, np.zeros((1,np.shape(ground)[0])), 0) #slow
        ground = np.append(ground, np.zeros((np.shape(ground)[0],1)), 1)
    
    if x1 == x2:
        ground[x1, min(y1,y2):max(y1,y2)+1] += 1
    elif y1 == y2:
        ground[min(x1,x2):max(x1,x2)+1, y1] += 1
    else:
        continue #print('Not a horizontal or vertical line')
print(len(np.where(ground > 1)[0]))

#Part 2
ground = np.zeros(np.shape(ground), int)
for line in lines:
    points = line.strip('\n').split(' -> ')
    x1, y1, x2, y2 = [int(x) for x in (points[0]+','+points[1]).split(',')]
    diff = max(abs(x2 - x1) ,abs(y2 - y1))
    dx = int((x2 - x1) / diff) 
    dy = int((y2 - y1) / diff)
    
    for j in range(diff+1):
        ground[x1+j*dx][y1+j*dy] += 1
    
print(len(np.where(ground > 1)[0]))
