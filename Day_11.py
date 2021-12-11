import numpy as np

f = open("input.txt", "r")
octo = np.asarray([[int(x) for x in line.strip('\n')] for line in f.readlines()])
f.close()
octo2 = octo.copy()

#Part 1
def step(arr):
    temp = np.zeros((np.shape(arr)[0]+2,np.shape(arr)[1]+2), dtype='i')
    temp[1:-1, 1:-1] = arr+1
    flashed = np.zeros(np.shape(arr), dtype='i')
    flashed[temp[1:-1, 1:-1] > 9] = 1
    n_flashed = 0
          
    while n_flashed < (flashed > 0).sum():
        n_flashed = (flashed > 0).sum()
        for (x, y) in np.argwhere(flashed == 1):
            temp[x:x+3, y:y+3] += 1
        flashed[temp[1:-1, 1:-1] > 9] += 1

    temp[temp>9] = 0
    return n_flashed, temp[1:-1, 1:-1]

n, steps = 0, 100
for i in range(steps):
    dn, octo = step(octo)
    n += dn

print(n)

#Part 2
n = 0
while True:
    dn, octo2 = step(octo2)
    n += 1
    if dn == np.shape(octo2)[0]*np.shape(octo2)[1]:
        break
    
print(n)
