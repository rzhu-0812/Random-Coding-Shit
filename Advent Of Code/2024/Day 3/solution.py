import re

with open('input.txt', 'r') as i:
    lines = i.readlines()

sum = 0

for line in lines:
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, line)
    
    for match in matches:
        a, b = map(int, match)
        sum += a * b

print(sum)

sum = 0
mul_enabled = True

for line in lines:
    pattern = r'mul\((\d+),(\d+)\)'
    do = r'do\(\)'
    dont = r'don\'t\(\)'

    matches = re.finditer(rf'{pattern}|{do}|{dont}', line)
    
    for match in matches:
        if match.group(0).startswith('mul'):
            if mul_enabled:
                a, b = map(int, match.groups())
                sum += a * b
        elif match.group(0) == 'do()':
            mul_enabled = True
        elif match.group(0) == 'don\'t()':
            mul_enabled = False

print(sum)
            