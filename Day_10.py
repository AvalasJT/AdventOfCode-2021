f = open("input.txt", "r")
lines = [x.strip('\n') for x in f.readlines()]
f.close()

#Part 1
close = {'(':')', '[':']', '{':'}', '<':'>'}
        
def reduce(seq):
#    print(seq)
    t_val = True

    while t_val and seq != '':
        if len(seq) == 1:
            return False, seq, 'Incomplete'
        if seq[0] in close:
            if seq[1] == close[seq[0]]: #can reduce
                return True, seq[2:], 'Reducing'
            elif seq[1] in close.values(): #wrong close
                return False, seq, 'Error: ' + close[seq[0]] + ' expected, but ' + seq[1] + ' found!'
            else: #new opener
                t_val, tseq, reason = reduce(seq[1:])
                if not t_val:
                    return t_val, tseq, reason
                seq = seq[0]+tseq
        else:
            return False, seq, 'Found early closing, go back'

def check(seq):
    t = True
    reason = 'Empty sequence'
    while t and seq != '':
        t, seq, reason = reduce(seq)
    return t, seq, reason
    
es = 0
es_val = {')':3, ']':57, '}':1197, '>':25137}
for l in lines:
    t, seq, reason = check(l)
    if 'Error:' in reason:
        es += es_val[reason.split()[4]]

print(es)


#Part 2
def repair(seq):
    rep = ''
    while True:
        t, s, __ = check(seq)
        if t:
            return rep
        rep += close[s]
        seq += close[s]


incpl = [l for l in lines if check(l)[2] == 'Incomplete']
ac_str = []

for il in incpl:
    ac_str.append(repair(il))
    
acs_val = {')':1, ']':2, '}':3, '>':4}
acs = []

for ac in ac_str:
    sc = 0
    for c in ac:
        sc *= 5
        sc += acs_val[c]
    acs.append(sc)

acs.sort()
print(acs[int((len(acs)-1)/2)])
