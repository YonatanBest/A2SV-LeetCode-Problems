class Solution:
    def isHappy(self, n: int) -> bool:
        final = 0
        i = 0
        arr = set()
        test = n
        while test != 1:
            if i < len(str(test)):
                final += int(str(test)[i])**2
                i += 1
            else: 
                test = final
                final = 0
                i = 0
                if test in arr:
                    return False
                arr.add(test)
        return True
