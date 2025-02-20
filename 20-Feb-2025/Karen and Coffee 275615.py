# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

r, valid, questions = map(int, input().split())
test = [0]*200002
for i in range(r):
    left, right = map(int, input().split())
    test[left] += 1
    test[right + 1] -= 1

for x in range(1, 200002):
    test[x] += test[x - 1]

for x in range(200002):
    if test[x] < valid:
        test[x] = 0
    else:
        test[x] = 1

for x in range(1, 200002):
    test[x] += test[x - 1]

for j in range(questions):
    left, right = map(int, input().split())
    print(test[right] - test[left-1])