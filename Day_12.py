f = open('input.txt', 'r')
connections = [x.strip('\n').split('-') for x in f.readlines()]
f.close()

caves = set([cave for connection in connections for cave in connection])
smallcaves = set([cave for cave in caves if all(c in 'abcdefghijklmnopqrstuvwxyz' for c in cave)])
connections = connections + [[x[1], x[0]] for x in connections]

#Part 1 + 2
def find_path_Joker(path, scv, Joker):
    if path[-1] == 'end':
        paths.append(path)
        return True

    for x in [co for co in connections if co[0] == path[-1]]:
        if (x[1] in scv and not Joker) or x[1] == 'start':
            continue
        elif x[1] in scv:   #Use Joker to visit sc twice
            find_path_Joker(path+[x[1]], scv, False)
        elif x[1] in smallcaves:
            find_path_Joker(path+[x[1]], scv+[x[1]], Joker)
        else: #big cave
            find_path_Joker(path+[x[1]], scv, Joker)
    return True

#Part 1
paths, scv = [], ['start'] #small caves visited
find_path_Joker(['start'],scv, False)
print(len(paths))
    
#Part 2
paths, scv = [], ['start']
find_path_Joker(['start'],scv, True)
print(len(paths))
