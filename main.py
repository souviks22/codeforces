import sys
sys.stdin = open('prime_subtractorization_input.txt','r')
for i in range(int(input())):
    n = int(input())
    prime = [True]*(n+1)
    prime[0] = prime[1] = False
    cur = 2
    while cur*cur <= n:
        if prime[cur]:
            for num in range(cur*cur,n+1,cur):
                prime[num] = False
        cur += 1
    count = int(n >= 5)
    for num in range(n+1):
        count += prime[num] and num+2 <= n and prime[num+2]
    print(f'Case #{i+1}: {count}')
