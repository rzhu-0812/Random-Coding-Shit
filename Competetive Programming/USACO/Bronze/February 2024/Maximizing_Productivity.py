from bisect import bisect_right

N, Q = map(int, input().split())
closing_hours = list(map(int, input().split()))
reach_time = list(map(int, input().split()))

latest_wakeup = [closing_hours[i] - reach_time[i] for i in range(N)]
latest_wakeup.sort()

results = []

for i in range(Q):
    V, S = map(int, input().split())
    
    count = bisect_right(latest_wakeup, S)
    
    if N - count >= V:
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))