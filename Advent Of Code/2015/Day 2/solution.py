with open('input.txt', 'r') as i:
    rects = i.readlines()

total_sa = 0

for rect in rects:
    dimensions = rect.strip().split('x')
    
    l, w, h = map(int, dimensions)
    
    total_sa += 2 * (l * w + w * h + h * l)
    total_sa += min(l * w, w * h, h * l)

print(total_sa)

total_ribbon = 0

for rect in rects:
    dimensions = rect.strip().split('x')
    
    l, w, h = map(int, dimensions)

    total_ribbon += min(2 * (l + w), 2 * (w + h), 2 * (h + l))
    total_ribbon += l * w * h

print(total_ribbon)