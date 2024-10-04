with open("lostcow.in", "r") as f:
    X, Y = map(int, f.readline().strip().split())

curr_pos = X
dist = 0
dir = 1
step_size = 1

while True:
    pos = X + dir * step_size
    
    if (Y <= curr_pos and Y >= pos) or (Y >= curr_pos and Y <= pos):
        dist += abs(Y - curr_pos)
        break
    else:
        dist += abs(pos - curr_pos)
    
    curr_pos = pos
    step_size *= 2
    dir *= -1

with open("lostcow.out", 'w') as f:
    f.write(str(dist) + "\n")