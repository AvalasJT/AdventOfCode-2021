import numpy as np

f = open("input.txt", "r")

#Part 1
ground = np.zeros((1,1,2), int)

for line in f:
    x1, y1, x2, y2 = [int(n) for n in line.replace(" -> ",",").split(",")]
    if max(x1, x2, y1, y2) > np.shape(ground)[0] - 1:
        ground = np.append(ground, np.zeros((max(x1, x2, y1, y2)+1 - np.shape(ground)[0],np.shape(ground)[0],2)), 0) #less slow
        ground = np.append(ground, np.zeros((np.shape(ground)[0],max(x1, x2, y1, y2)+1 - np.shape(ground)[1],2)), 1)
    
    if x1 == x2:
        ground[x1, min(y1,y2):max(y1,y2)+1,0] += 1
    elif y1 == y2:
        ground[min(x1,x2):max(x1,x2)+1, y1,0] += 1

#Part 2
    diff = max(abs(x2 - x1) ,abs(y2 - y1))
    dx = int((x2 - x1) / diff) 
    dy = int((y2 - y1) / diff)
    
    for j in range(diff+1):
        ground[x1+j*dx, y1+j*dy, 1] += 1
        
print(len(np.where(ground[:,:,0] > 1)[0]))    
print(len(np.where(ground[:,:,1] > 1)[0]))
