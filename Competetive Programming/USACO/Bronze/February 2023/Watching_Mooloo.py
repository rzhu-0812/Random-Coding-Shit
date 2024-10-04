N, K = map(int, input().split())
days = list(map(int, input().split()))
sub_cost = 0

for i in range(N):
    if i == 0:
        sub_cost += K + 1
    else:
        extend_sub = days[i] - days[i-1]
        new_sub = K + 1
        sub_cost += min(extend_sub, new_sub)
        
print(sub_cost)