for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    cur = max(a)
    maxi = []
    for _ in range(m):
        op, l, r = input().split()
        l, r = int(l), int(r)
        if l <= cur <= r:
            cur += 1 if op == '+' else -1
        maxi.append(cur)
    print(*maxi)
