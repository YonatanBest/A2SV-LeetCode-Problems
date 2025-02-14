# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
for i in range(int(input())):
    length = int(input())
    arr = list(map(int, input().split()))
    dic = Counter(arr)
    total = float("inf")
    rep = []
    for j in dic:
        rep.append(dic[j])
    rep.sort()
    total_sum = sum(rep)
    sub = 0
    for k in range(len(rep)):
        temp = total_sum - rep[k]*(len(rep) - k)
        total = min(total, temp)
    print(total)