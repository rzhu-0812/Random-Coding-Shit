with open("shuffle.in", "r") as f:
    lines = f.readlines()

N = int(lines[0].strip())
shuffle = list(map(int, lines[1].strip().split()))
ids = list(lines[2].strip().split())

rev_shuffle = [0] * N
for i in range(N):
    rev_shuffle[shuffle[i] - 1] = i

curr_ids = ids[:]

for _ in range(3):
    new_ids = [0] * N
    for i in range(N):
        new_ids[rev_shuffle[i]] = curr_ids[i]
    curr_ids = new_ids

with open("shuffle.out", 'w') as f:
    for id in curr_ids:
        f.write(f"{id}\n")
