# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import defaultdict
length = int(input())
 
dic = defaultdict(int)
 
 
for i in range(length):
    left, right = map(int, input().split())
    dic[left] += 1
    dic[right + 1] -= 1
dic = sorted(dic.items())
temp = 0
new = []
 
"""
        1:5, 2:2, 
[(1, 1), (2, 2), (4, 1), (5, 1), (8, 0)]
 
"""
 
for i in dic:
    temp += i[1]
    new.append((i[0], temp))
 
final = defaultdict(int)
for i in range(1, len(new)):
    final[new[i - 1][1]] += new[i] [0] - new[i - 1][0]
 
 
res = []
 
for i in range(length):
    if i+1 in final:
        res.append(final[i+1])
    else:
        res.append(0)
        
print(*res)