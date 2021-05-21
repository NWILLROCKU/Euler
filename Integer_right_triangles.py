import math

triplets = []
p_max = 1000
for leg1 in range(1, p_max+1):
    for leg2 in range(leg1, p_max+1):
        if leg1 + leg2 > p_max:
            break
        root = math.sqrt(leg1**2 + leg2**2)
        if root==int(root) and leg1 + leg2 + root <= p_max:
            triplets.append([leg1, leg2, root])

p = []
cnt = []
for row in triplets:
    if sum(row) in p:
        i = p.index(sum(row))
        cnt[i] += 1
    else:
        p.append(sum(row))
        cnt.append(1)
            
        
