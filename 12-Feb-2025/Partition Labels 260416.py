# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]].add(i)
            else:
                dic[s[i]] = set([i])
        arr = []
        for i in dic:
            arr.append([min(dic[i]), max(dic[i])])
        arr.sort()
        for i in range(1, len(arr)):
            if arr[i][0] < arr[i - 1][1]:
                arr[i] = [arr[i - 1][0], max(arr[i][1], arr[i - 1][1])]
                arr[i - 1] = None
            else:
                pass
        ans = []
        for i in arr:
            if i != None:
                ans.append((i[1] - i[0]) + 1)
        return ans