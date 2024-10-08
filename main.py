for _ in range(int(input())):
    n = int(input())
    child = list(map(int,input().split()))
    c1, c2 = map(int,input().split())
    def get_order(c):
        order = [-1]*n
        order[c] = 0
        while child[c] != -1 and order[child[c]] == -1:
            order[child[c]] = 1 + order[c]
            c = child[c]
        return order
    o1, o2 = get_order(c1), get_order(c2)
    cm, mini = -1, n+1
    for i in range(n):
        if o1[i] == -1 or o2[i] == -1:
            continue
        level = max(o1[i],o2[i])
        if level < mini:
            cm = i
            mini = level
    print(cm)
