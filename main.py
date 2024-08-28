from sys import stdout
for _ in range(int(input())):
    n = int(input())
    edges = []
    marked = [False]*(n+1)
    def find(a,b):
        if marked[a] and marked[b]:
            return
        print(f'? {a} {b}')
        stdout.flush()
        x = int(input())
        if x == a:
            edges.append(a)
            edges.append(b)
        else:
            find(a,x)
            find(x,b)
        marked[a] = marked[b] = True

    for v in range(2,n+1):
        if not marked[v]:
            find(1,v)
    print('!',end=' ')
    print(*edges)    
