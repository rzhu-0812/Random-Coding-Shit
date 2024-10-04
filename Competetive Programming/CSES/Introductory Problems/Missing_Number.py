n = int(input())
list_num = list(map(int, input().split()))
 
present = [False] * (n + 1)
 
for num in list_num:
    if 1 <= num <= n:
        present[num] = True
 
for i in range(1, n + 1):
    if not present[i]:
        print(i)
        break
