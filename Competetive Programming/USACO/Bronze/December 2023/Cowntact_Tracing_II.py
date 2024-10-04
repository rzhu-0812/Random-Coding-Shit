n = int(input().strip())
s = input().strip()

segments = []
region = 0

for i in range(n):
    if s[i] == '1':
        region += 1
    else:
        if region > 0:
            segments.append(region)
        region = 0

if region > 0:
    segments.append(region)

minBlock = [float('inf'), float('inf')]
minEnd = float('inf')
sind = 0
eind = len(segments) - 1

if s[0] == '1':
    minEnd = min(minEnd, segments[0])
    sind += 1

if s[-1] == '1':
    minEnd = min(minEnd, segments[eind])
    eind -= 1

for i in range(sind, eind + 1):
    minBlock[segments[i] % 2] = min(minBlock[segments[i] % 2], segments[i])

daySpread = min(minEnd * 2 - 1, min(minBlock[0] - 1, minBlock[1]))
numInfected = 0

for block in segments:
    numInfected += (block + daySpread - 1) // daySpread

print(numInfected)