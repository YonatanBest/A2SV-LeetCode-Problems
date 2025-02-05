class Solution:
    def printVertically(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        arr = list(map(str, s.split()))
        max_index = 0
        for i in range(len(arr)):
            if len(arr[max_index]) < len(arr[i]):
                max_index = i
        ans = [""]*len(arr[max_index])
        for j in range(len(arr[max_index])):
            for k in arr:
                if j < len(k):
                    ans[j] += k[j]
                else:
                    ans[j] += " "

        for x in range(len(ans)):
            i = len(ans[x]) - 1
            while i >= 0:
                if ans[x][i] != " ":
                    ans[x] = ans[x][0 : i + 1]
                    break
                else:
                    i -= 1
        return ans