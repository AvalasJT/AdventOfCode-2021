import numpy as np

areas = []
command = []
with open('input.txt', 'r') as f:
    for line in f:
        command.append(line.strip().split()[0])
        area = line.strip().split()[1].split(',')
        area = [x.split('=')[1].split('..') for x in area]
        area = [[int(x), int(y)] for x,y in area]
        areas.append(area)

#%% #Part 1
reactor = np.zeros((101,101,101), 'i')

for i in range(len(command)):
    if max([y for x in areas[i] for y in x]) > 50 or min([y for x in areas[i] for y in x]) < -50:
        continue
    if command[i] == 'on':
        reactor[areas[i][0][0]+50:areas[i][0][1]+51, areas[i][1][0]+50:areas[i][1][1]+51, areas[i][2][0]+50:areas[i][2][1]+51] = 1
    else:
        reactor[areas[i][0][0]+50:areas[i][0][1]+51, areas[i][1][0]+50:areas[i][1][1]+51, areas[i][2][0]+50:areas[i][2][1]+51] = 0

print(len(np.argwhere(reactor == 1)))

#%% #Part 2
x_vals, y_vals, z_vals = set(), set(), set()
x_conv, y_conv, z_conv = dict(), dict(), dict()
x_anti_conv, y_anti_conv, z_anti_conv = dict(), dict(), dict()
for x, y, z in areas:   
    x_vals.add(x[0])
    x_vals.add(x[0]-1)
    x_vals.add(x[1])
    x_vals.add(x[1]+1)
    y_vals.add(y[0])
    y_vals.add(y[0]-1)
    y_vals.add(y[1])
    y_vals.add(y[1]+1)
    z_vals.add(z[0])
    z_vals.add(z[0]-1)
    z_vals.add(z[1])
    z_vals.add(z[1]+1)

i = 0
for x in sorted(x_vals):
    i += 1
    x_conv[x] = i
    x_anti_conv[i] = x
    
i = 0
for y in sorted(y_vals):
    i += 1
    y_conv[y] = i
    y_anti_conv[i] = y
    
i = 0
for z in sorted(z_vals):
    i += 1
    z_conv[z] = i
    z_anti_conv[i] = z

transformed_areas = []
for a in areas:
    ix, iy, iz = a
    transformed_areas.append([[x_conv[x] for x in ix], [y_conv[y] for y in iy], [z_conv[z] for z in iz]])
      
reactor = np.zeros((len(x_conv)+1,len(y_conv)+1,len(z_conv)+1), 'bool')
on_list = []
for i in range(len(command)):
    if command[i] == 'on':
        reactor[transformed_areas[i][0][0]:transformed_areas[i][0][1]+1, transformed_areas[i][1][0]:transformed_areas[i][1][1]+1, transformed_areas[i][2][0]:transformed_areas[i][2][1]+1] = True
    else:
        reactor[transformed_areas[i][0][0]:transformed_areas[i][0][1]+1, transformed_areas[i][1][0]:transformed_areas[i][1][1]+1, transformed_areas[i][2][0]:transformed_areas[i][2][1]+1] = False
                        
def volume(x, y, z):
    return (x_anti_conv[x+1]-x_anti_conv[x])*(y_anti_conv[y+1]-y_anti_conv[y])*(z_anti_conv[z+1]-z_anti_conv[z])

on_volume = 0
for i in range(np.shape(reactor)[2]):
    for x,y in np.argwhere(reactor[:,:,i] == True):
        on_volume += volume(x,y,i)
    print(i, 'of', np.shape(reactor)[2])
    
print(on_volume)
