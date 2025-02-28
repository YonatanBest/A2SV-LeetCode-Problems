# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

length = int(input())
arr = list(map(int, input().split()))
arr.sort()
if len(arr) % 2:
    print(arr[len(arr)//2])
else:
    print(arr[len(arr)//2 - 1])