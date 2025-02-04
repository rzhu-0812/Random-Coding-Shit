with open('socdist.in', 'r') as fin:
    N, M = map(int, fin.readline().split())
    intervals = []
    for _ in range(M):
        a, b = map(int, fin.readline().split())
        intervals.append((a, b))

intervals.sort()

def is_possible(D):
    count = 0
    prev_pos = None
    for a, b in intervals:
        if prev_pos is None:
            first_pos = a
        else:
            first_pos = max(a, prev_pos + D)
        if first_pos > b:
            continue
        num_cows = (b - first_pos) // D + 1
        count += num_cows
        prev_pos = first_pos + (num_cows - 1) * D
        if count >= N:
            return True
    return count >= N

low = 1
high = intervals[-1][1] - intervals[0][0]
ans = 0

while low <= high:
    mid = (low + high) // 2
    if is_possible(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

with open('socdist.out', 'w') as fout:
    fout.write(str(ans) + '\n')