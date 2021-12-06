f = open("input.txt", "r")
fish = [int(x) for x in f.readline().strip('\n').split(',')]

#Part 1
def evolve(fish, days):
    f = []
    for i in range(9):
        f.append(fish.count(i))
    
    for d in range(days):
        temp = f.pop(0)
        f.append(temp)
        f[6] += temp

    return sum(f)

print(evolve(fish, 80))

#Part 2
print(evolve(fish, 256))
