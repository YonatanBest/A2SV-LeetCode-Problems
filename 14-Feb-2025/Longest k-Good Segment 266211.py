# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict, Counter
n, k = map(int, input().split())
arr = list(map(int, input().split()))
 
if n <= k:
    print(1, n)
else:
    dic = defaultdict(int)
    left = 0
    ans = []
    
    for right in range(n):
        
        dic[arr[right]] += 1
        
        while len(dic) > k:
            
            dic[arr[left]] -= 1
            if dic[arr[left]] == 0:
                del dic[arr[left]]
            left += 1
        if not ans: 
            ans = [left, right]
        elif ans[1] - ans[0] < right - left:
            ans = [left, right]
    print(ans[0] + 1, ans[1] + 1)