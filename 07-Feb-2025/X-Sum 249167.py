# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

for m in range(int(input())):
    row, col = map(int, input().split())
    mat = []
    for k in range(row):
        mat.append(list(map(int, input().split())))
    disum = {}
    disub = {}
    for i in range(row):
        for j in range(col):
            if i + j in disum:
                
                disum[i + j].append(mat[i][j])
            else:
                disum[i + j] = [mat[i][j]]  
    for i in range(row):
        for j in range(col):
            if i - j in disub:
                disub[i - j].append(mat[i][j])
            else:
                disub[i - j] = [mat[i][j]]
    max_sum = 0
    for i in range(row):
        for j in range(col):
            add = sum(disum[i + j])
            sub = sum(disub[i - j])
            max_sum = max(max_sum, add + sub - mat[i][j])
    print(max_sum)