class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = {}
        tdic = {}
        for i in s:
            if i in sdic:
                sdic[i] += 1
            else:
                sdic[i] = 1
        for j in t:
            if j in tdic:
                tdic[j] += 1
            else:
                tdic[j] = 1
        if sdic == tdic:
            return True
        else:
            return False