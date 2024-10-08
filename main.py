for _ in range(int(input())):
    n = int(input())
    child = list(map(int,input().split()))
    weights = [0]*n
    for i, c in enumerate(child):
        if c == -1:
            continue
        weights[c] += i
    maxi = weights.index(max(weights))
    print(maxi)
