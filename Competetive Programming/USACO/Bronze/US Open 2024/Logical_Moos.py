N, Q = map(int, input().split())
bool_s = input()

output = []

for _ in range(Q):
    l = input().split()
    s = bool_s
    
    start, end, value = int(l[0]), int(l[1]), "True" if l[2] == "true" else "False"
    
    bool_l = bool_s.split()
    bool_l[start - 1:end] = [value]
    n = " ".join(bool_l).replace("false", "False").replace("true", "True")

    if eval(n) == eval(value):
        output.append("Y")
    else:
        output.append("N")

print("".join(output))

# O(N * Q)