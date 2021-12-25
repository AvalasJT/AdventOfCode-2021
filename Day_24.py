# Initially solved per hand and found the relations for my problem
# This solution is from redditor Diderikdm .. :( .. I just wanted to try it... it works..
 
ALU_seq = []
sub = []
with open('input.txt', 'r') as f:
    for line in f:
        if line.strip() == 'inp w':
            if not sub == []:
                ALU_seq.append(sub)
            sub = []
        else:
            sub.append(line.strip().split())
    ALU_seq.append(sub)

#Part 1 + 2        
all_the_same = [True]*len(ALU_seq[0])
for i in range(len(ALU_seq[0])):
    for j in range(1,len(ALU_seq)):
        if ALU_seq[0][i] != ALU_seq[j][i]:
            all_the_same[i] = False

diffs = []
for i in range(len(ALU_seq)):
    sub = []
    for j, same in enumerate(all_the_same):
        if not same:
            sub.append(int(ALU_seq[i][j][2]))
    diffs.append(sub)
    
stack, max_no, min_no = [], [0] * 14, [0] * 14
for i, x in enumerate(ALU_seq):
    if diffs[i][0] == 1: #calculation term survives
        stack.append((i, diffs[i][2]))
    else:
        old_i, old_val = stack.pop()
        delta = old_val + diffs[i][1]
        if delta < 0:
            i, old_i, delta = old_i, i, -delta
        max_no[i], max_no[old_i] = 9, 9 - delta
        min_no[old_i], min_no[i] = 1, 1 + delta
        
print(''.join([str(x) for x in max_no]))
print(''.join([str(x) for x in min_no]))
