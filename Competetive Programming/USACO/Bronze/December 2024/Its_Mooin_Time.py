def possible_moos(N, F, s):
    poss_m = set()

    for i in range(N):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if s[i] == c:
                continue

            mod_s = s[:i] + c + s[i+1:]
            poss_m.update(find_moos(mod_s, F))

    return sorted(poss_m)

def find_moos(s, F):
    moos = set()
    L = len(s)

    substring_counts = {}
    for i in range(L - 2):
        substring = s[i:i+3]
        if substring not in substring_counts:
            substring_counts[substring] = 0
        substring_counts[substring] += 1

    for i in range(L - 2):
        if s[i] == s[i + 1]:
            continue

        if i + 2 < L and s[i + 1] == s[i + 2]:
            moo = s[i] + s[i + 1] + s[i + 2]
            if moo in substring_counts and substring_counts[moo] >= F:
                moos.add(moo)

    return moos

N, F = map(int, input().split())
s = input()

result = possible_moos(N, F, s)

print(len(result))
for moo in result:
    print(moo)