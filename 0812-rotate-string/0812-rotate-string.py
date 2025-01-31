class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        check = []
        for i in goal:
            check.append(i)
        test = []
        for j in s:
            test.append(j)
        if check == test:
            return True
        else:
            tested = test.copy()
            checker = True
            while tested != test or checker:
                checker = False
                tested.append(tested[0])
                tested.pop(0)
                if check == tested:
                    return True
        return False