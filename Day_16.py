with open('input.txt', 'r') as f:
    l = f.readline().strip()
    message = bin(int(l,16))[2:].zfill(len(l)*4) 

def get_literal_Value(m):
    last = False
    val = ''
    while not last:
        if m[0] == '0':
            last = True
        m = m[1:]
        val += m[:4]
        m = m[4:]
    val = int(val,2)
    return val, m

def get_sum_V(m):
    if len(m) < 11:
        return 0, m
    V, m = int(m[:3],2), m[3:]
    T, m = int(m[:3],2), m[3:]
    V_sum = V
    
    if T == 4:
        __, m = get_literal_Value(m)
    else:
        L_T_ID, m = int(m[0]), m[1:]
        if L_T_ID == 0: #legnth of subpackage
            len_sub_pack, m = int(m[:15],2), m[15:]
            sub_m, m = m[:len_sub_pack], m[len_sub_pack:]
            while sub_m != '':
                sub_V, sub_m = get_sum_V(sub_m)
                V_sum += sub_V
        else: #number of subpackages
            num_sub_pack, m = int(m[:11],2), m[11:]
            for i in range(num_sub_pack):
                sub_V, m = get_sum_V(m)
                V_sum += sub_V
    return V_sum, m

V_sum, mes = get_sum_V(message)
print(V_sum)

#Part 2
def interprete(m):
    if len(m) < 11:
        return 0, m
    T, m = int(m[3:6],2), m[6:]
    
    if T == 4:
        Val, m = get_literal_Value(m)
    else:
        L_T_ID, m = int(m[0]), m[1:]
        sub_Vals = []
        if L_T_ID == 0: #legnth of subpackage
            len_sub_pack, m = int(m[:15],2), m[15:]
            sub_m, m = m[:len_sub_pack], m[len_sub_pack:]
            while sub_m != '':
                sub_Val, sub_m = interprete(sub_m)
                sub_Vals.append(sub_Val)
        else:
            num_sub_pack, m = int(m[:11],2), m[11:]
            for i in range(num_sub_pack):
                sub_Val, m = interprete(m)
                sub_Vals.append(sub_Val)
                
        if T == 0:
            Val = sum(sub_Vals)
        elif T == 1:
            Val = 1
            for sV in sub_Vals:
                Val *= sV
        elif T == 2:
            Val = min(sub_Vals)
        elif T == 3:
            Val = max(sub_Vals)
        elif T == 5:
            Val = int(sub_Vals[0] > sub_Vals[1])
        elif T== 6:
            Val = int(sub_Vals[0] < sub_Vals[1])
        elif T== 7:
            Val = int(sub_Vals[0] == sub_Vals[1])
        else:
            Val = -999
            print('Invalid Type')

    return Val, m
        
Val, mes = interprete(message)
print(Val)
