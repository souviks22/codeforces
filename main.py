import sys
sys.stdin = open('subsonic_subway_input.txt','r')
for i in range(int(input())):
    n = int(input())
    a = [tuple(map(int,input().split()) )for _ in range(n)]
    def pos(speed):
        for i, (start, end) in enumerate(a):
            cur = (i+1)/speed
            if cur < start:
                return -1
            if cur > end:
                return 1
        return 0
    lo, hi, res = 0, 10**18, -1
    while True:
        mid = int(((lo+hi)/2)*10**6)/10**6
        if mid == lo or mid == hi:
            break
        cur = pos(mid)
        if cur == -1:
            hi = mid
        elif cur == 1:
            lo = mid
        else:
            res = mid
            hi = mid
    print(f'Case #{i+1}: {res}')
