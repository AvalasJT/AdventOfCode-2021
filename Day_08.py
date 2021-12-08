f = open("input.txt", "r")
lines = f.readlines()
f.close()

#Part 1
n = 0
for line in lines:
    inp, outp = [x for x in line.strip('\n').split(' | ')[0].split()], [x for x in line.strip('\n').split(' | ')[1].split()]

    for o in outp:
        if len(o) in [2, 3, 4, 7]:
            n += 1
            
print(n)

#Part 2
possible_seg = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sum_out = 0
for line in lines:
    inp, outp = [x for x in line.strip('\n').split(' | ')[0].split()], [x for x in line.strip('\n').split(' | ')[1].split()]
    numbers = ['' for i in range(10)]
    dic = {} #segment: letter in this line

    for i in inp:  #1, 4, 7 und 8 zuordnen
        if len(i) == 2:
            numbers[1] = i
        elif len(i) == 3:
            numbers[7] = i
        elif len(i) == 4:
            numbers[4] = i
        elif len(i) == 7:
            numbers[8] = i

    for c in numbers[7]:    #Seg. a zuordnen
        if not c in numbers[1]:
            dic['a'] = c
             
    for i in inp:  #3 zuordnen
        if len(i) == 5: #2, 3, 5
            if numbers[1][0] in i and numbers[1][1] in i:
                numbers[3] = i
                break
    
    for i in inp:  #6 zuordnen
        if len(i) == 6: #0, 6, 9
            if not (numbers[1][0] in i and numbers[1][1] in i):
                numbers[6] = i
                break
    
    if not numbers[1][0] in numbers[6]: #Seg. c zuordnen
        dic['c'] = numbers[1][0]
    else:
        dic['c'] = numbers[1][1]
        
    for i in inp:  #Seg. d zuordnen und 0 zuordnen
        if len(i) == 6: #0, 6, 9
            if i == numbers[6]:
                continue
            for c in possible_seg:
                if not c in i:  #immer das fehlende segment anschauen
                    if c in numbers[3]:
                        dic['d']= c
                        numbers[0] = i
                        break
            if 'd' in dic:
                break
            
    for i in inp:  #9 zuordnen
        if len(i) == 6: #0, 6, 9
            if i != numbers[0] and i != numbers[6]:
                numbers[9] = i
    
    for i in inp:  #Seg. g zuordnen 9 - 4 - a
        temp = numbers[9]
        for c in numbers[4]:
            temp = temp.replace(c, '')
        temp = temp.replace(dic['a'], '')
        dic['g'] = temp
        
    for c in possible_seg:  #Seg. e zuordnen -9
        if not c in numbers[9]:  
            dic['e'] = c
            break

    for i in inp:   #2 zuordnen
        if len(i) == 5: #2, 3, 5
            is_two = True
            for c in ['a', 'c', 'd', 'e', 'g']: # = 2
                if not dic[c] in i:
                    is_two = False
            if is_two:
                numbers[2] = i
                break
    
    for i in inp:   #5 zuordnen - letzte Zahl
        if not i in numbers:
            numbers[5] = i
            break

    temp = numbers[3] #Seg. f zuordnen 3 - 2
    for c in numbers[2]:  
        temp = temp.replace(c, '')
    dic['f'] = temp    
    
    for c in possible_seg: #Seg. b zuordnen - letztes Segment
        if not c in dic.values():
            dic['b'] = c
            break

    digets_translate = {}
    for i, n in enumerate(numbers):
        digets_translate[''.join(sorted(numbers[i]))] = str(i)
        
    output_val = ''    
    for o in outp:
        output_val += digets_translate[''.join(sorted(o))]

    sum_out += int(output_val)
    
print(sum_out)
