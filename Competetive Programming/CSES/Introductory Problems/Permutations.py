N = int(input())

if N == 1:
    print(1)
elif N == 2 or N == 3:
    print("NO SOLUTION")
else:
    evens = list(range(2, N + 1, 2))
    odds = list(range(1, N + 1, 2))
    
    print(*evens, *odds)