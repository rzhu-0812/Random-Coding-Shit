N = int(input())
A = list(map(int, input().split()))

ans = 0
contribution = 0
cnt_ops = 0

for i in range(N):
    contribution += cnt_ops
    A[i] += contribution
    
    cur_ops = -A[i]
    ans += abs(cur_ops)
    cnt_ops += cur_ops
    contribution += cur_ops

print(ans)