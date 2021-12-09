import numpy as np

f = open("input.txt", "r")
h = np.asarray([[int(x) for x in line.strip('\n')] for line in f.readlines()])

#Part 1
def local_min(arr):
    test = np.ones((np.shape(arr)[0]+2,np.shape(arr)[1]+2), dtype='i')*(np.amax(arr)+1)
    test[1:-1,1:-1] = np.asarray(arr, dtype='i')
    bool_min = ((test < np.roll(test,  1, 0)) &
                (test < np.roll(test, -1, 0)) &
                (test < np.roll(test,  1, 1)) &
                (test < np.roll(test, -1, 1)))[1:-1, 1:-1]
    return bool_min

def risk_values(arr):
    return (arr + 1) * local_min(arr)
    
print(sum(sum(risk_values(h))))

#Part 2
def basin_size(arr, x):
    test = np.zeros((np.shape(arr)[0]+2,np.shape(arr)[1]+2), dtype='i')
    test[x[0]+1][x[1]+1] = 1
    while True:
        test2 = (test + (np.roll(test,  1, 0) + np.roll(test,  -1, 0)
                        +np.roll(test,  1, 1) + np.roll(test,  -1, 1)))[1:-1, 1:-1]
        test2[test2 > 0] = 1
        test2[arr == 9] = 0
        if np.all(test[1:-1, 1:-1] == test2):
            break
        test[1:-1, 1:-1] = test2
    return sum(sum(test))

b_sizes = [basin_size(h, x) for x in np.argwhere(local_min(h))]
b_sizes.sort(reverse=True)
print(b_sizes[0]*b_sizes[1]*b_sizes[2])
