class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        dic = {"a":1, "e":2, "i":3, "o":4, "u":5}
        cnt = 0
        maxcnt = 0
        number = 1
        x = True
        for i in dic:
            if i not in word:
                return 0
        for i in word:
            if x:
                if dic[i] == number:
                    cnt += 1
                x = False
            else:
                if dic[i] == number:
                    cnt += 1
                elif dic[i] - number == 1:
                    cnt += 1
                    number += 1
                else:
                    if number == 5 and cnt >= 5:
                        maxcnt = max(maxcnt, cnt)
                    cnt = 0
                    number = 1
                    x = True
                    if dic[i] == number:
                        cnt += 1
                        x = False
        if number == 5 and cnt >= 5:
            maxcnt = max(maxcnt, cnt)
        return maxcnt
