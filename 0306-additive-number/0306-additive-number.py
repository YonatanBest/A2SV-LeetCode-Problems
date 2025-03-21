class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        self.check = False
        def backtrack(i, path):
            if len(path) > 2 and int(path[len(path) - 1]) != int(path[len(path) - 2]) + int(path[len(path) - 3]):
                return
            if len(num) == i:
                test = True
                for k in range(2, len(path)):
                    if int(path[k]) != int(path[k - 1]) + int(path[k - 2]):
                        test = False
                if test and len(path) > 2 and (len(path) != 3 or int(path[2]) == int(path[0]) + int(path[1])):
                    self.check = True
            nums = ""
            for j in range(i, len(num)):
                nums += num[j]
                if len(nums) != 1 and nums[0] == "0":
                    return
                path.append(nums)
                backtrack(j + 1, path)
                path.pop()
            return
        backtrack(0, [])
        return self.check