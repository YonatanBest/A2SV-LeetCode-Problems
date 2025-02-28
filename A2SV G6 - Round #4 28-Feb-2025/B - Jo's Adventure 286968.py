# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

import copy
buildings, questions = map(int, input().split())
arr = list(map(int, input().split()))
prefix = copy.deepcopy(arr)
suffix = copy.deepcopy(arr)
for i in range(1, len(arr)):
    if arr[i-1] - arr[i] > 0:
        prefix[i] = arr[i-1] - arr[i]
        suffix[i] = 0
    else:
        suffix[i] = abs(arr[i-1] - arr[i])
        prefix[i] = 0
    if i - 1 == 0:
            prefix[i - 1] = 0
            suffix[i - 1] = 0
pre = copy.deepcopy(prefix)
suf = copy.deepcopy(suffix)
 
for k in range(1, len(prefix)):
    pre[k] += pre[k - 1]
for l in range(1, len(suffix)):
    suf[l] += suf[l - 1]
for i in range(questions):
    left, right = map(int, input().split())
    if right == left:
        print(0)
    elif right > left:
        if left - 1 >= 0:
            print(pre[right-1] - pre[left - 1])
        else:
            print(pre[right-1])
    else:
        if right - 1 >= 0:
            print(suf[left-1] - suf[right - 1])
        else:
            print(suf[left-1])