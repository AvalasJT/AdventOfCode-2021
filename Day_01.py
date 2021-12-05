list = []

f = open("input.txt", "r")
list = [int(x) for x in f]
f.close()


#Part 1
n = 0
last = list[0]

for x in list[1:]:
    if x > last:
        n += 1
    last = x
    
print(n)

  
    
#Part 2
n = 0
last = sum(list[0:3])
a = 0

for i in range(1, len(list)-2):
    a = sum(list[i:i+3])

    if a > last:
        n += 1
    last = a
    
print(n)
