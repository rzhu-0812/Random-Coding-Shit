T = int(input())

for _ in range(T):
    N = int(input())
    fav = list(map(int, input().split()))
    result = []
    
    for i in range(len(fav) - 1):
        if fav[i] == fav[i + 1] or (i < len(fav) - 2 and fav[i] == fav[i + 2]):
            result.append(fav[i])
            
    result = sorted(list(set(result)))
    
    if len(result) == 0:
        result = [-1]
        
    print(*result)
