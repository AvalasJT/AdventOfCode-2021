rules = {}
with open('input.txt', 'r') as f:
    poly = f.readline().strip()
    elements = set(list(poly))
    __ = f.readline()
    for l in f:
        rules[l.strip().split(' -> ')[0]] = l.strip().split(' -> ')[1]
        elements.add(l.strip().split(' -> ')[1])
        
#Part 1 + 2
is_created_by = {}
for key, val in rules.items():
    is_created_by[key] = [k for k in rules if k in key[:1]+val+key[1:]]
        
def print_diff_after_n_steps(steps):
    key_count = {k:poly.count(k) for k in rules}
    e_count = {e:poly.count(e) for e in elements}

    for s in range(steps):
        new_key_count = {k:0 for k in rules}
        for key in rules:
            for e in elements:
                if rules[key] == e:
                    e_count[e] += key_count[key]
                    
            for new_key in is_created_by[key]:
                new_key_count[new_key] += key_count[key]  
        key_count = new_key_count.copy()
    
    print(max(e_count.values())-min(e_count.values()))
    return

print_diff_after_n_steps(10)
print_diff_after_n_steps(40)
