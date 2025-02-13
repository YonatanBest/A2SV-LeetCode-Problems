# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        j = 0
        check = Counter(p)
        dic = defaultdict(int)
        ans = set()
        while j < len(s):
            if dic == check:
                ans.add(i)
            if s[j] in check:
                if s[j] not in dic:
                    dic[s[j]] += 1
                else:
                    while s[j] in dic and dic[s[j]] >= check[s[j]]:
                        dic[s[i]] -= 1
                        if dic[s[j]] == 0:
                            del dic[s[j]]
                        i += 1
                    dic[s[j]] += 1
            else:
                i = j + 1
                dic = defaultdict(int)
            j += 1
        if dic == check:
            ans.add(i)
        return list(ans)