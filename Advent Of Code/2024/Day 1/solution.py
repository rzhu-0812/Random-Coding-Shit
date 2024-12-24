with open('input.txt', 'r') as i:
    lines = i.readlines()
    
location_list1 = []
location_list2 = []

for line in lines:
    split_line = line.split()
    
    location_list1.append(split_line[0])
    location_list2.append(split_line[1])

location_list1.sort()
location_list2.sort()

# Part 1

sum_diff = 0

for i in range(len(location_list1)):
    sum_diff += abs(int(location_list1[i]) - int(location_list2[i]))
    
print(sum_diff)


# Part 2

sim_score = 0

for i in range(len(location_list1)):
    sim_score += location_list2.count(location_list1[i]) * int(location_list1[i])
    
print(sim_score)
