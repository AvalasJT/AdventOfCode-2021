#Part 1
p1pos = 4 
p2pos = 8  

p1score = 0
p2score = 0

dice = 0

while p1score < 1000 and p2score < 1000:
    steps = 3*dice + 6
    dice += 3
    if (dice/3)%2 == 1:
        p1pos = 10 if (p1pos + steps)%10 == 0 else (p1pos + steps)%10
        p1score += p1pos
    else:
        p2pos = 10 if (p2pos + steps)%10 == 0 else (p2pos + steps)%10
        p2score += p2pos
    
print(min(p1score, p2score)*dice)

#%%
#Part 2
p1pos = 4 
p2pos = 8  

possible_steps = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
win_rolls_p1, win_rolls_p2, loose_rolls_p1, loose_rolls_p2 = [], [], [], []
p1_win_ways, p2_win_ways, p1_loose_ways, p2_loose_ways = {}, {}, {}, {}

p1_wins = p2_wins = 0

def calc_possible_rolls(pos, score, rolls, win_rolls, loose_rolls):
    for s in possible_steps:
        if calc_score(pos, score, s) >= 21:
            win_rolls.append(rolls + [s])
        else:
            loose_rolls.append(rolls + [s])
            calc_possible_rolls(calc_pos(pos, s), calc_score(pos, score, s), rolls+[s], win_rolls, loose_rolls)
            
def calc_score(pos, score, steps):
    return score + calc_pos(pos, steps)

def calc_pos(pos, steps):
    return 10 if (pos + steps)%10 == 0 else (pos + steps)%10

def cals_n_ways(rolls, ways):
    for roll in rolls:
        rounds = len(roll)
        if not rounds in ways:
            ways[rounds] = 0
        way = 1
        for r in roll:
            way *= possible_steps[r]
        ways[rounds] += way
    
calc_possible_rolls(p1pos, 0, [], win_rolls_p1, loose_rolls_p1)
calc_possible_rolls(p2pos, 0, [], win_rolls_p2, loose_rolls_p2)

cals_n_ways(win_rolls_p1, p1_win_ways)
cals_n_ways(win_rolls_p2, p2_win_ways)
cals_n_ways(loose_rolls_p1, p1_loose_ways)
cals_n_ways(loose_rolls_p2, p2_loose_ways)

for p1 in p1_win_ways:
    p1_wins += p1_win_ways[p1]*p2_loose_ways[p1-1]
for p2 in p2_win_ways:
    if p2 in p1_loose_ways:
        p2_wins += p2_win_ways[p2]*p1_loose_ways[p2]
            
print(max(p1_wins, p2_wins))
