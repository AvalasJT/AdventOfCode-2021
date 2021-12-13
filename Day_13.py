import numpy as np

dots = []
folds = []
with open('input.txt', 'r') as f:
    for l in f:
        sl = l.strip().split()
        if sl == []:
            continue
        if sl[0] == 'fold':
            folds.append(sl[2].split('='))
        else:
            dots.append(tuple([int(x) for x in sl[0].split(',')]))
            
#Part 1
max_x, max_y = max([x for x,y in dots]), max([y for x,y in dots])

page = np.zeros((max_x+1, max_y+1), 'i')
for d in dots:
    page[d] = 1
    
def fold(fold, page):
    if fold[0] == 'x':
        result = np.zeros((int(fold[1]),np.shape(page)[1]), 'i')
        result[:int(fold[1]), :] += page[:int(fold[1]), :]
        result[-(np.shape(page)[0]-int(fold[1])-1):, :] += np.flip(page[int(fold[1])+1:, :], 0)
    else:
        result = np.zeros((np.shape(page)[0],int(fold[1])), 'i')
        result[:, :int(fold[1])] += page[:, :int(fold[1])] 
        result[:, -(np.shape(page)[1]-int(fold[1])-1):] += np.flip(page[:, int(fold[1])+1:], 1)
    result[result > 1] = 1
    return result

page = fold(folds[0],page)
print(np.sum(page))

#Part 2
for f in folds[1:]:
    page = fold(f, page)

print(np.transpose(page)) #Interpretation of letters is still manual :(
