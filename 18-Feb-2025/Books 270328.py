# Problem: Books - https://codeforces.com/contest/279/problem/B

length, time = map(int, input().split())
books = list(map(int, input().split()))


time_consumed = 0
max_books = 0
i = 0
j = 0
while j < length:
    time_consumed += books[j]
    while time_consumed > time:
        time_consumed -= books[i]
        i += 1
    max_books = max(max_books, j - i + 1)
    j += 1
print(max_books)