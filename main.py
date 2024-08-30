import math
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] %= gcd
    arr.sort()
    mini = arr[-1] - arr[0]
    for i in range(n - 1):
        mini = min(mini, arr[i] + gcd - arr[i + 1])
    print(mini)