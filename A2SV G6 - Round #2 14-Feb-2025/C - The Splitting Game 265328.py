# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter, defaultdict
for times in range(int(input())):
    length = int(input())
    arr = input()
    ans = 0
    dic = Counter(arr)
    dic2 = defaultdict(int)
    j = 0
    ans = float("-inf")
    while j < len(arr):
        dic[arr[j]] -= 1
        if dic[arr[j]] == 0:
            del dic[arr[j]]
        dic2[arr[j]] += 1
        j += 1
        ans = max(ans, len(dic) + len(dic2))
    print(ans)