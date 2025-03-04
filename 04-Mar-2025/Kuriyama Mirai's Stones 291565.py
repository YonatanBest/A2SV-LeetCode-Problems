# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

length = int(input())
costs = list(map(int, input().split()))
costs_inc = sorted(costs)
 
for k in range(1, length):
    costs[k] += costs[k - 1]
    costs_inc[k] += costs_inc[k - 1]
 
for i in range(int(input())):
    typ, l, r = map(int, input().split())
    l -= 1
    r -= 1
    if typ == 1:
        print(costs[r] - (costs[l - 1] if l > 0 else 0))
    else:
        print(costs_inc[r] - (costs_inc[l - 1] if l > 0 else 0))