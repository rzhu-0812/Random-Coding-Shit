N, Q = map(int, input().split())

rows = [[N] * N for _ in range(N)]
cols = [[N] * N for _ in range(N)]
depth = [[N] * N for _ in range(N)]

count = 0

for _ in range(Q):
    x, y, z = map(int, input().split())

    if rows[x][y] > 0:
        rows[x][y] -= 1
        if rows[x][y] == 0:
            count += 1

    if cols[x][z] > 0:
        cols[x][z] -= 1
        if cols[x][z] == 0:
            count += 1
    
    if depth[y][z] > 0:
        depth[y][z] -= 1
        if depth[y][z] == 0:
            count += 1

    print(count)
