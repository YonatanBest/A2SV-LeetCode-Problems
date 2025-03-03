class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 0
        check = False
        for i in range(len(nums) - 2, -1, -1):
            
            if check:
                if nums[i] > count:
                    check = False
                    count = 0
                else:
                    count += 1

            if nums[i] == 0 and not check:
                count += 1
                check = True
            print(count, i, nums[i])
        if check:
            return False
        else:
            return True
