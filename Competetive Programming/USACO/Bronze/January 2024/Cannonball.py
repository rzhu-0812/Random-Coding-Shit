N, X = map(int, input().split())
    
pad = [(0, 0)] * (N + 1)
vis = [False] * (N + 1)

for i in range(1, N + 1):
    pad[i] = tuple(map(int, input().split()))

dir = 1
power = 1
ans = 0

for reps in range(5000000):
    if not (1 <= X <= N):
        break
    if pad[X][0] == 1 and power >= pad[X][1] and not vis[X]:
        vis[X] = True
        ans += 1
    
    if pad[X][0] == 0:
        dir *= -1
        power += pad[X][1]
    
    X += dir * power

print(ans)