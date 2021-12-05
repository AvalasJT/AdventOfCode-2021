import numpy as np

list = []

f = open("input.txt", "r")
list = [x.strip("\n") for x in f]
f.close()

#Part 1
ones = np.zeros(len(list[0]))
zeroes = np.zeros(len(list[0]))
g, e = '', ''

for x in list:
    for i in range(len(x)):    
        if x[i] == '0':
            zeroes[i] += 1
        else:
            ones[i] += 1

for i in range(len(ones)):
    if ones[i] == zeroes[i]:
        print('Invalid Input')
        exit()
    
    if ones[i] > zeroes[i]:
        g += '1'
        e += '0'
    else:
        g += '0'
        e += '1'

gamma = int(g, 2)
epsilon = int(e, 2)

print(gamma*epsilon)
    
#Part 2
O2 = list.copy()
CO2 = list.copy()

def find_most_common(list, i):
    o = 0
    z = 0
    
    if i > len(list[0]):
        print('Invalid input')
        return -1
    else:
        
        for x in list:
            if x[i] == '0':
                z += 1
            else:
                o += 1
        
        if o == z:
            return 0.5
        elif o > z:
            return 1
        else:
            return 0
                      
for i in range(len(O2[0])):
    if find_most_common(O2, i) > 0:
        O2 = [x for x in O2 if x[i] == '1']
    else:
        O2 = [x for x in O2 if x[i] == '0']

    if len(O2) == 1:
        break

for i in range(len(CO2[0])):
    if find_most_common(CO2, i) > 0:
        CO2 = [x for x in CO2 if x[i] == '0']
    else:
        CO2 = [x for x in CO2 if x[i] == '1']
    
    if len(CO2) == 1:
        break
        
O2_gen = int(O2[0], 2)
CO2_scrub = int(CO2[0], 2)
print(O2_gen*CO2_scrub)
