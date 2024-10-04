Q = int(input())
moo_str = [input() for _ in range(Q)]
changes = []

for s in moo_str:
    s = s.strip()
    if len(s) < 3:
        changes.append("-1")
    else:
        if "MOO" in s:
            changes.append(str(len(s) - 3))
        elif "OOO" in s or "MOM" in s:
            changes.append(str(len(s) - 2))
        elif "OOM" in s:
            changes.append(str(len(s) - 1))
        else:
            changes.append("-1")
    
print("\n".join(changes))