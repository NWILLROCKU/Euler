ds = []
d = 0
next_d = 1
n = 1
while d <= 1e6:
    n_str = str(n)
    if d + len(n_str)>=next_d:
        diff = next_d - d
        ds.append(n_str[diff-1])
        next_d *= 10
    d += len(n_str)
    n += 1
    
