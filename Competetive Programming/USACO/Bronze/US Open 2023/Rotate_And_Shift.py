import sys

input = sys.stdin.readlines

data = input()

N, K, T = map(int, data[0].split())
active_pos = list(map(int, data[1].split())) + [N]

results = [-1] * N

for i in range(K):
    start = active_pos[i]
    end = active_pos[i + 1]
    
    for j in range(start, end):
        T_prime = T - (j - start + 1)
        
        if T_prime >= 0:
            increase_time = 1 + T_prime // (end - start)
            end_pos = (j + increase_time * (end - start)) % N
        else:
            end_pos = j
        
        results[end_pos] = j

print(" ".join(map(str, results)))
