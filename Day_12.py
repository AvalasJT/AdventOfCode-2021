f = open('input_test.txt', 'r')
connections = [x.strip().split('-') for x in f.readlines()]
connections = connections + [[x[1], x[0]] for x in connections]

#Part 1 + 2
def find_path_Joker(path, Joker):
    if path[-1] == 'end':
        paths.append(path)
        return

    for x in [co for co in connections if co[0] == path[-1]]:
        if not x[1].islower():  #Big cave
            find_path_Joker(path+[x[1]], Joker)
        elif (x[1] in path and not Joker) or x[1] == 'start':   #Dead end
            continue
        elif x[1] in path:   #Use Joker to visit sc twice
            find_path_Joker(path+[x[1]], False)
        else:   #new sc
            find_path_Joker(path+[x[1]], Joker)
            
    return

#Part 1
paths = []
find_path_Joker(['start'], False)
print(len(paths))
    
#Part 2
paths = []
find_path_Joker(['start'], True)
print(len(paths))
