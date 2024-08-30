for _ in range(int(input())):
    l, r = map(int,input().split())
    cur, ops = l, 0
    while cur <= r-2:
        if cur % 2 == 0:
            cur += 1
        else:
            cur += 3
            ops += 1
    print(ops)
