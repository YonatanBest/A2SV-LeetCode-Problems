from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = Counter(s1)
        dic2 = defaultdict(int)
        i = 0
        j = 0
        count = 0
        for j in range(len(s2)):
            if len(s1) == count:
                if dic == dic2:
                    return True
                dic2[s2[i]] -= 1
                count -= 1
                if dic2[s2[i]] == 0:
                    del dic2[s2[i]]
                i += 1
            dic2[s2[j]] += 1
            count += 1
        if len(s1) == count:
            if dic == dic2:
                return True
        return False
