# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

for i in range(int(input())):
    a_length = int(input())
    a = list(map(int, input().split()))
    b_length = int(input())
    b = list(map(int, input().split()))
    a_idx = 0
    b_idx = 0
    sum_a = 0
    sum_b = 0
    max_a = 0
    max_b = 0
    max_sum = 0
    while a_idx < a_length and b_idx < b_length:
        sum_a += a[a_idx]
        sum_b += b[b_idx]
        max_a = max(max_a, sum_a)
        max_b = max(max_b, sum_b)
        a_idx += 1
        b_idx += 1
    while a_idx < a_length:
        sum_a += a[a_idx]
        max_a = max(max_a, sum_a)
        a_idx += 1
    while b_idx < b_length:
        sum_b += b[b_idx]
        max_b = max(max_b, sum_b)
        b_idx += 1
 
    print(max(max_a, max_b, max_a + max_b))