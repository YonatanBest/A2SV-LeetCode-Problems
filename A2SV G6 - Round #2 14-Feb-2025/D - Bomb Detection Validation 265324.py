# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

row_total, col_total = map(int, input().split())
matrix = []
for i in range(row_total):
    matrix.append(list(input()))
dir = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
check = True
for row in range(row_total):
    for col in range(col_total):
        count = 0
        if matrix[row][col] == ".":
            for di in dir:
                if -1 < row + di[0] < row_total and -1 < col + di[1] < col_total and matrix[row + di[0]][col + di[1]] == "*":
                    count += 1
            if count != 0:
                check = False
                break
        elif matrix[row][col].isalnum():
            for di in dir:
                if -1 < row + di[0] < row_total and -1 < col + di[1] < col_total and matrix[row + di[0]][col + di[1]] == "*":
                    count += 1
            if count != int(matrix[row][col]):
                check = False
                break
        else:
            pass
    if not check:
        break
if check:
    print("YES")
else:
    print("NO")