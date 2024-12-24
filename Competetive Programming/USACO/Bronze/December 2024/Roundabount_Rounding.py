T = int(input())
ranges = [[45, 49], [445, 499], [4445, 4999], [44445, 49999], [444445, 499999], [4444445, 4999999], [44444445, 49999999], [444444445, 499999999], [4444444445, 4999999999]]
quick_counts = [5, 60, 615, 6170, 61725, 617280, 6172835, 61728390, 617283900]

for _ in range(T):
    N = int(input())
    
    if N < 45:
        print(0)
        continue
    elif N >= 45 and N <= 49:
        print(5 - (49 - N))
        continue
    elif N < 100:
        print(5)
        continue
    
    p = len(str(N))

    if N > ranges[p - 2][1] and N < ranges[p - 1][0]:
        print(quick_counts[p - 2])
    elif N > ranges[p - 3][1] and N < ranges[p - 2][0]:
        print(quick_counts[p - 3])
    else:
        print(quick_counts[p - 3] + (N - ranges[p - 2][0]) + 1)
