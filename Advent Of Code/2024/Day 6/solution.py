with open('input.txt', 'r') as i:
    lines = i.readlines()

map = [list(line.strip()) for line in lines]

direction = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

curr_pos = None
curr_dir = None
for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] in direction:
            curr_pos = [row, col]
            curr_dir = map[row][col]
            break
    if curr_pos:
        break

visited = set()
visited.add(tuple(curr_pos))

while True:
    dir_offset = direction[curr_dir]
    next_pos = [curr_pos[0] + dir_offset[0], curr_pos[1] + dir_offset[1]]

    if not (0 <= next_pos[0] < len(map) and 0 <= next_pos[1] < len(map[0])):
        break
    
    if map[next_pos[0]][next_pos[1]] == '#':
        if curr_dir == '^':
            curr_dir = '>'
        elif curr_dir == '>':
            curr_dir = 'v'
        elif curr_dir == 'v':
            curr_dir = '<'
        elif curr_dir == '<':
            curr_dir = '^'
    else:
        curr_pos = next_pos
        visited.add(tuple(curr_pos))

for pos in visited:
    row, col = pos
    if map[row][col] not in direction:
        map[row][col] = 'X'

print(len(visited))