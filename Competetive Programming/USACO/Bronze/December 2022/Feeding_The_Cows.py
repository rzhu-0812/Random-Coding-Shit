T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    patches = ["."] * N
    G, H = -1, -1
    S = input()
    
    for i, char in enumerate(S):
        if char == "G" and G < i:
            if i + K >= len(patches):
                if patches[i] != ".":
                    patches[i - 1] = "G"
                else:
                    patches[i] = "G"
                
                G = N
            else:
                patches[i + K] = "G"
                G = i + 2 * K
                
        elif char == "H" and H < i:
            if i + K >= len(patches):
                if patches[i] != ".":
                    patches[i - 1] = "H"
                else:
                    patches[i] = "H"
                
                H = i + K
            else:
                patches[i + K] = "H"
                H = i + 2 * K
    
    print(N - patches.count("."))
    print("".join(patches))