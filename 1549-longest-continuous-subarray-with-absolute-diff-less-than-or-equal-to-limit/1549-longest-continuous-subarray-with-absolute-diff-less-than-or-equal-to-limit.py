class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decreasing = deque()
        increasing = deque()
        max_len = 0
        i = 0
        j = 0
        while j < len(nums):
            while decreasing and decreasing[-1] < nums[j]:
                decreasing.pop()
            while increasing and increasing[-1] > nums[j]:
                increasing.pop()
            decreasing.append(nums[j])
            increasing.append(nums[j])

            while decreasing and decreasing[0] - increasing[0] > limit:
                if nums[i] == decreasing[0]:
                    decreasing.popleft()
                if nums[i] == increasing[0]:
                    increasing.popleft()
                i += 1
            max_len = max(max_len, j - i + 1)
            j += 1
            
        return max_len