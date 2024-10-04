N = int(input())
cow_tuitions = [int(num) for num in input().split()]

tuitions = [0] * 1000001

lowest_tuition = 0
total_tuition = 0
students = 0

for num in cow_tuitions:
    tuitions[num] += 1

for i in range(1000000, 0, -1):
    students += tuitions[i]
    
    if students * i >= total_tuition:
        total_tuition = students * i
        lowest_tuition = i

print(total_tuition, lowest_tuition)
    