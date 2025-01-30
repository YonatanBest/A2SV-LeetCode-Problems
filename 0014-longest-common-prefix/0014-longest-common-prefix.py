class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        arr = []
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                arr.append(strs[0][i])
            else:
                break
        return "".join(arr)