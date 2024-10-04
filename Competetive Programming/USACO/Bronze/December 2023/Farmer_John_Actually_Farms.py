T = int(input())

for _ in range(T):
    N = int(input())
    H = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    T = [int(x) for x in input().split()]
    
    order = [i for i in range(N)]
    order.sort(key=lambda x: T[x])
    
    min_moves = 0
    
    for idx in range(N - 1):
        i = order[idx]
        j = order[idx + 1]
        
        if H[i] < H[j] and A[i] > A[j]:
            min_moves = max(min_moves, ((H[j] - H[i] + 1) + (A[i] - A[j]) - 1) // (A[i] - A[j]))
            
    for i in range(N):
        H[i] += A[i] * min_moves
        
    for idx in range(N - 1):
        i = order[idx]
        j = order[idx + 1]
        if H[i] <= H[j]: 
            min_moves = -1

    print(min_moves)