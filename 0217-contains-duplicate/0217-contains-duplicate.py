class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = defaultdict(int)
        for num in nums:
            if num in duplicate:
                return True
            duplicate[num] += 1
        return False 