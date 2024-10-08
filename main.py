for _ in range(int(input())):
    n = int(input())
    child = list(map(int,input().split()))
    maxi = length = 0
    value = [None]*n
    for i in range(n):
        if value[i]:
            continue
        cur, marked = i, [False]*n
        marked[cur] = True
        value[cur] = (0,0)
        while child[cur] != -1 and not value[child[cur]]:
            s, l = value[cur]
            value[child[cur]] = (s + cur, l + 1)
            cur = child[cur]
            marked[cur] = True
        if child[cur] == -1 or not marked[child[cur]]:
            continue
        s1, l1 = value[cur]
        s2, l2  = value[child[cur]]
        s, l = s1 + cur - s2, l1 + 1 - l2
        if s > maxi:
            maxi = s
            length = l
    print(length)
        



        

