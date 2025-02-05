# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        dic = Counter(chars)
        for i in words:
            temp = Counter(i)
            check = True
            for j in temp:
                if (j not in dic) or dic[j] < temp[j]:
                    check = False
                    break
            if check:
                res += len(i)
        return res