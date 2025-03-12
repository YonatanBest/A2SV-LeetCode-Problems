# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

for i in range(int(input())):
    length = int(input())
    arr = input()
    ones = []
    zeros = []
    count = 0
    ans = []
    for i in range(length):
        if arr[i] == "1":
            if not zeros:
                temp = len(ones) + 1
                ones.append(temp)
            else:
                temp = zeros.pop()
                ones.append(temp)
        else:
            if not ones:
                temp = len(zeros) + 1
                zeros.append(temp)
            else:
                temp = ones.pop()
                zeros.append(temp)
        count = max(temp, count)
        ans.append(temp)
    print(count)
    print(*ans)