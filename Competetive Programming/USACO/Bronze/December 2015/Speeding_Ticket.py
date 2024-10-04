with open("speeding.in", "r") as f:
    i = f.readlines()

n, m = map(int, i[0].strip().split())
r = [tuple(map(int, line.strip().split())) for line in i[1: 1 + n]]
b = [tuple(map(int, line.strip().split())) for line in i[1 + n:]]

r_s = [] 
b_s = []

speed = 0
p = 0

for (l, s) in r:
    r_s += l * [s]

for (l, s) in b:
    b_s += l * [s]

while p < 100:
    if b_s[p] - r_s[p] > speed:
        speed = b_s[p] - r_s[p]
    p += 1

with open("speeding.out", 'w') as f:
    f.write(str(speed))