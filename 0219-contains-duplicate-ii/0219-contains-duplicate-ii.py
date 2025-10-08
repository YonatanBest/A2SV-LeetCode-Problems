class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        identify_duplicate = defaultdict(int)
        for j in range(len(nums)):
            if nums[j] in identify_duplicate and abs(identify_duplicate[nums[j]] - j) <= k:
                return True
            identify_duplicate[nums[j]] = j
        return False
            