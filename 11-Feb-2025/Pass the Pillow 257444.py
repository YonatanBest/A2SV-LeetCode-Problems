# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        check = True
        times = 1
        while times <= time:
            if i < n and check:
                i += 1
            elif i > 1:
                i -= 1
                check = False
            else:
                i += 1
                check = True
            times += 1
        return i
        
