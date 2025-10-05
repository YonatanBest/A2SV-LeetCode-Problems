class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = Counter(s)
        for i in t:
            if i in dic:
                dic[i] -= 1
                if dic[i] == 0:
                    del dic[i]
            else:
                return False
        return not dic