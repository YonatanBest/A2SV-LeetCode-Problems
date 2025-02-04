from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = Counter(s)
        tdict = Counter(t)
        if sdict == tdict:
            return True
        else:
            return False