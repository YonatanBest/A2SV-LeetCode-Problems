# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        final = []
        dic = dict(reversed(sorted(dic.items(), key=lambda item: item[1])))
        for i in dic:
            for j in range(dic[i]):
                final.append(i)
        return "".join(final)