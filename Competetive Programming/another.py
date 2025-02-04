import itertools

def solve():
    T = int(input())  # Read the number of test cases
    
    # The 7 labels (with their coefficient vectors in terms of A, B, C):
    labels = [
        (1, 0, 0),  # L1 = A
        (0, 1, 0),  # L2 = B
        (0, 0, 1),  # L3 = C
        (1, 1, 0),  # L4 = A + B
        (1, 0, 1),  # L5 = A + C
        (0, 1, 1),  # L6 = B + C
        (1, 1, 1)   # L7 = A + B + C
    ]
    
    # Function to compute determinant of a 3x3 matrix
    def det3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

    # Precompute valid (invertible) label combinations
    valid_label_combos = []
    for combo in itertools.combinations(range(7), 3):
        mat = [labels[i] for i in combo]
        d = det3(mat)
        if d != 0:
            valid_label_combos.append((combo, d))
    
    results = []
    
    for _ in range(T):
        N = int(input())  # Read N
        xs = list(map(int, input().split()))  # Read N numbers
        xs_set = set(xs)
        xs_sorted = sorted(xs)
        found = set()
        
        for (combo, d) in valid_label_combos:
            m = [labels[i] for i in combo]
            
            for chosen in itertools.combinations(xs_sorted, 3):
                for perm in itertools.permutations(chosen):
                    v = perm  # Right-hand side
                    
                    # Compute determinants using Cramer's rule
                    M_A = [(v[0], m[0][1], m[0][2]),
                           (v[1], m[1][1], m[1][2]),
                           (v[2], m[2][1], m[2][2])]
                    M_B = [(m[0][0], v[0], m[0][2]),
                           (m[1][0], v[1], m[1][2]),
                           (m[2][0], v[2], m[2][2])]
                    M_C = [(m[0][0], m[0][1], v[0]),
                           (m[1][0], m[1][1], v[1]),
                           (m[2][0], m[2][1], v[2])]
                    
                    dA, dB, dC = det3(M_A), det3(M_B), det3(M_C)

                    # Check integer divisibility
                    if dA % d != 0 or dB % d != 0 or dC % d != 0:
                        continue
                    A_val, B_val, C_val = dA // d, dB // d, dC // d

                    # Must satisfy A ≤ B ≤ C and be positive
                    if A_val <= 0 or B_val <= 0 or C_val <= 0:
                        continue
                    if not (A_val <= B_val <= C_val):
                        continue
                    
                    # Check full set S
                    full_set = {A_val, B_val, C_val, A_val + B_val, 
                                A_val + C_val, B_val + C_val, A_val + B_val + C_val}
                    
                    if xs_set.issubset(full_set):
                        found.add((A_val, B_val, C_val))
        
        results.append(str(len(found)))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()
