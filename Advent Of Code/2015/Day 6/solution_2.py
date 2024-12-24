import re

with open('input.txt', 'r') as i:
    lines = i.read()

lights = [[0 for _ in range(1000)] for _ in range(1000)]

t_on = r'turn on (\d+),(\d+) through (\d+),(\d+)'
t_off = r'turn off (\d+),(\d+) through (\d+),(\d+)'
toggle = r'toggle (\d+),(\d+) through (\d+),(\d+)'

matches = re.finditer(rf'{t_on}|{t_off}|{toggle}', lines)

def turn_on(sX, sY, eX, eY):
    for i in range(sX, eX + 1):
        for j in range(sY, eY + 1):
            lights[i][j] += 1

def turn_off(sX, sY, eX, eY):
    for i in range(sX, eX + 1):
        for j in range(sY, eY + 1):
            if lights[i][j] > 0:
                lights[i][j] -= 1

def toggle_light(sX, sY, eX, eY):
    for i in range(sX, eX + 1):
        for j in range(sY, eY + 1):
            lights[i][j] += 2

commands = []

for match in matches:
    groups = match.groups()
    if groups[:4] != (None, None, None, None):
        x1, y1, x2, y2 = map(int, groups[:4])
        commands.append(['turn on', (x1, y1, x2, y2)])
    elif groups[4:8] != (None, None, None, None):
        x1, y1, x2, y2 = map(int, groups[4:8])
        commands.append(['turn off', (x1, y1, x2, y2)])
    elif groups[8:] != (None, None, None, None):
        x1, y1, x2, y2 = map(int, groups[8:])
        commands.append(['toggle', (x1, y1, x2, y2)])

for command in commands:
    startX, startY, endX, endY = command[1]
    
    if command[0] == 'turn on':
        turn_on(startX, startY, endX, endY)
    elif command[0] == 'turn off':
        turn_off(startX, startY, endX, endY)
    elif command[0] == 'toggle':
        toggle_light(startX, startY, endX, endY)

lights_on = sum(sum(row) for row in lights)
print(lights_on)
