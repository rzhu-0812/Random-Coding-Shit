N, M = map(int, input().split())
cows = [[int(s), int(t), int(c)] for s, t, c in [input().split() for _ in range(N)]]
acs = [[int(a), int(b), int(p), int(m)] for a, b, p, m in [input().split() for _ in range(M)]]

min_cost = sum(ac[3] for ac in acs)

for used_ac in range(2 ** M):
    cool = [0] * 101
    cost = 0
    
    for i in range(M):
        if used_ac & (2 ** i):
            cost += acs[i][3]
            for j in range(acs[i][0], acs[i][1] + 1):
                cool[j] += acs[i][2]
    
    valid = True
    
    for i in range(N):
        valid = valid and all(cool[j] >= cows[i][2] for j in range(cows[i][0], cows[i][1] + 1))
    
    if valid:
        min_cost = min(min_cost, cost)

print(min_cost)