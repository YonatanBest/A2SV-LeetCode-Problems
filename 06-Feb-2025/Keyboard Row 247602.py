# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic1 = {"q":1, "w":1, "e":1, "r":1, "t":1, "y":1, "u":1, "i":1, "o":1, "p":1}
        dic2 = {"a":1, "s":1, "d":1, "f":1, "g":1, "h":1, "j":1, "k":1, "l":1}
        dic3 = {"z":1, "x":1, "c":1, "v":1, "b":1, "n":1, "m":1}
        arr = [dic1, dic2, dic3]
        ans = []
        final = []
        for k in words:
            for j in range(3):
                for i in k:
                    if i.lower() not in arr[j]:
                        ans.append(j)
                        break
            if len(ans) != 3:
                final.append(k)
            ans = []
        return final