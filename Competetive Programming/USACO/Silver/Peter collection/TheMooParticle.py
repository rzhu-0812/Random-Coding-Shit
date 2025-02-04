import heapq

with open("moop.in", "r") as fin:
    i = fin.readlines()

N = int(i[0])
particles = [tuple(map(int, x.strip().split())) for x in i[1:]]

particles.sort()

heap = []

for _, y in particles:
    if heap and heap[0] <= y:
        min_rep = heapq.heappop(heap)
        while heap and heap[0] <= y:
            min_rep = min(min_rep, heapq.heappop(heap))
        heapq.heappush(heap, min_rep)
    else:
        heapq.heappush(heap, y)

with open("moop.out", "w") as fout:
    fout.write(str(len(heap)))