N = int(input())
a = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]

Q = int(input())
queries = []
for _ in range(Q):
    l, r, x = map(int, input().split())
    queries.append((l, r, x))

results = []
for l, r, x in queries:
    diff = x
    
    bessie_extra = 0
    elsie_extra = 0
    left, right = l - 1, r - 1
    
    while left <= right:
        mid = (left + right) // 2
        hay_mid = prefix[mid + 1] - prefix[l - 1]
        
        if diff + hay_mid >= 0:
            bessie_extra += a[mid]
            left = mid + 1
        else:
            elsie_extra += a[mid]
            right = mid - 1
    
    final_diff = x + bessie_extra - elsie_extra
    results.append(final_diff)

print("\n".join(map(str, results)))