with open("pails.in", "r") as f:
    X, Y, M = map(int, f.readline().strip().split())

max_num = 0

for i in range(M // X + 1):
    diff = M - (i * X)
    max_num = max(max_num, (i * X) + Y * (diff // Y))

with open("pails.out", 'w') as f:
    f.write(f"{max_num}")

