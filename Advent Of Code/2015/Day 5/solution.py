with open('input.txt', 'r') as i:
    lines = i.readlines()
    
nice_str = 0

for line in lines:
    vowels = set("aeiou")
    forbidden = {"ab", "cd", "pq", "xy"}

    vowel_count = sum(1 for char in line if char in vowels)
    if vowel_count < 3:
        continue

    has_double = any(line[i] == line[i+1] for i in range(len(line) - 1))
    if not has_double:
        continue

    has_forbidden = any(bad in line for bad in forbidden)
    if has_forbidden:
        continue
    
    nice_str += 1

print(nice_str)


nice_str = 0

for line in lines:
    pair = any(line[i:i+2] in line[i+2:] for i in range(len(line) - 1))
    repeat = any(line[i] == line[i+2] for i in range(len(line) - 2))

    if pair and repeat:
        nice_str += 1

print(nice_str)