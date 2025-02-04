def main():
    # Read N and M
    N, M = map(int, input().split())
    
    # Read the preferences of each cow
    cows = []
    for _ in range(N):
        f, s = map(int, input().split())
        cows.append((f, s))
    
    # Initialize the result array
    result = [0] * N
    
    # Initialize a set to keep track of available cereals
    available = set(range(1, M + 1))
    
    # Initialize a running count of cows that have taken cereals
    count = 0
    
    # Iterate from the end to the beginning
    for i in range(N - 1, -1, -1):
        f, s = cows[i]
        if f in available:
            available.remove(f)
            count += 1
        elif s in available:
            available.remove(s)
            count += 1
        # Store the count for the current i
        result[i] = count
    
    # Print the results
    for i in range(N):
        print(result[i])

if __name__ == "__main__":
    main()