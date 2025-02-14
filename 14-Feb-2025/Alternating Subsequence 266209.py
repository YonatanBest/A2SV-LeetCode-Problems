# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

for i in range(int(input())):
    length = int(input())
    arr = list(map(int, input().split()))
    dic = arr[0]   # -2
    left = 0
    for right in range(1, length):       
        if arr[left] > 0 and arr[right] > 0:
            if arr[left] < arr[right]:
                dic -= arr[left]
                dic += arr[right]
                left = right
            continue
        elif arr[left] < 0 and arr[right] < 0:
            if arr[left] < arr[right]:
                dic -= arr[left]
                dic += arr[right]
                left = right
            continue
        else:
            dic += arr[right]
            left = right
            
    print(dic)