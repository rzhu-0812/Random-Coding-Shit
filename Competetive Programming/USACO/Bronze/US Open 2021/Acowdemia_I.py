N, L = map(int, input().split())
citations = list(map(int, input().split()))

citations.sort(reverse=True)

def can_achieve_h(h):
    needed_citations = 0
    for i in range(h):
        if citations[i] < h:
            needed_citations += h - citations[i]
        if needed_citations > L:
            return False
    return True

low, high = 0, N
result = 0

while low <= high:
    mid = (low + high) // 2
    if can_achieve_h(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1
    
print(result)
