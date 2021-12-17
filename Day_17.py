with open('input.txt', 'r') as f:
    __, __, xrange, yrange = f.readline().strip().split()
    xrange, yrange = xrange.split('=')[1], yrange.split('=')[1]
    xrange, yrange = xrange.split('..'), yrange.split('..')
    xrange, yrange = [int(x.strip(',')) for x in xrange], [int(y) for y in yrange]
    
#Part 1 + 2
def check(vx, vy):
    x = y = ymax = 0
    while True:
        x += vx
        y += vy
        if y > ymax:
            ymax = y
        if x > max(xrange) or y < min(yrange):
            return False, 0
        if (min(xrange) <= x <= max(xrange)) and (min(yrange) <= y <= max(yrange)):
            return True, ymax
        if vx > 0:  #never < 0 ?
            vx -= 1
        vy -= 1
    
ymax = bvx = bvy = n = 0
for vx in range(500):
    for vy in range(min(yrange), 500):
        T, tempymax = check(vx,vy)
        if T:
            n += 1
            if tempymax > ymax:
                ymax, bvx, bvy = tempymax, vx, vy
                
print(ymax, bvx, bvy)
print(n)
