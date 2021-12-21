import numpy as np

img = []
with open('input.txt', 'r') as f:
    enhance, _ = f.readline().strip().replace('.','0').replace('#','1'), f.readline()
    for line in f:
        img.append([x for x in line.strip().replace('.','0').replace('#','1')])
        
#Part 1 + 2
def calc_steps(steps, img):
    in_img = np.zeros((350,350), 'i')
    out_img = np.zeros((350,350), 'i')
    in_img[125:225,125:225] = np.asarray(img)

    for s in range(steps):
        for x in range(1+s, 349-s):
            for y in range(1+s, 349-s):
                key = int(''.join([str(x) for x in in_img[x-1:x+2,y-1:y+2].reshape((1,9))[0]]), 2)
                out_img[x,y] = int(enhance[key])

        in_img[:] = out_img[:]
              
    return len(np.argwhere(out_img[60:290,60:290] == 1))

print(calc_steps(2, img))
print(calc_steps(50, img))
