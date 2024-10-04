N, M = map(int, input().split())
cows = list(map(int, input().split()))
canes = map(int, input().split())

for cane in canes:
    if cane <= cows[0]:
        cows[0] += cane
    else:
        cane_dist = 0
        for i in range(N):
            if cows[i] > cane_dist:
                eat = min(cows[i], cane)
                cows[i] += eat - cane_dist
                cane_dist = eat

for cow in cows:
    print(cow)