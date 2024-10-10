class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i_d = {}
        j_d = {}
        for i in s:
            if i in i_d:
                i_d[i] += 1
            else:
                i_d[i] = 1
        for j in t:
            if j in j_d:
                j_d[j] += 1
            else:
                j_d[j] = 1
        for k in j_d:
            if k not in i_d:
                return k
            if j_d[k] != i_d[k]:
                return k