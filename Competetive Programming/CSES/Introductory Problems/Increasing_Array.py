n = int(input())
list_num = list(map(int, input().split()))
prev = None
min_move = 0
 
for i in range(n):
    if prev and list_num[i] < prev:
        min_move += prev - list_num[i]
    else:
        prev = list_num[i]
 
print(min_move)