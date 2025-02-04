with open("cowsignal.in", "r") as f:
    i = f.readlines()

M, N, K = map(int, i[0].strip().split())
S = [line.strip() for line in i[1:]]

new_str = []

for i, st in enumerate(S):
    new_str += K * [st]

for i in range(K * M):
    new_str[i] = "".join([char * K for char in new_str[i]])

new_str = "\n".join(new_str)

with open("cowsignal.out", 'w') as f:
    f.write(new_str)