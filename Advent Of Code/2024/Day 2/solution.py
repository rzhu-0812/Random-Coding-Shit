with open('input.txt', 'r') as i:
    lines = i.readlines()

def part1(lines):
    count = 0

    for line in lines:
        curr_report = list(map(int, line.split()))
        if is_valid_report(curr_report):
            count += 1

    print(count)

def part2(lines):
    count = 0
    
    for line in lines:
        curr_report = list(map(int, line.split()))
        if is_valid_report(curr_report):
            count += 1
            continue
        
        valid_with_dampener = False;
        
        for i in range(len(curr_report)):
            modified_report = [x for j, x in enumerate(curr_report) if j != i]

            if is_valid_report(modified_report):
                valid_with_dampener = True
                break

        if valid_with_dampener:
            count += 1
            
    print(count)

def is_valid_report(report):
    differences = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]

    if not all(1 <= diff <= 3 for diff in differences):
        return False

    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    return increasing or decreasing

part1(lines)
part2(lines)