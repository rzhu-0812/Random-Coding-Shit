N = int(input())
cow_t = list(map(int, input().split()))

tuitions = {}

for t in cow_t:
    tuitions[t] = tuitions.get(t, 0) + 1

students = 0
min_tuition = 0
max_profit = 0

sorted_t = sorted(tuitions.keys(), reverse=True)

for t in sorted_t:
    students += tuitions[t]
    
    if students * t >= max_profit:
        min_tuition = t
        max_profit = students * t

print(max_profit, min_tuition)