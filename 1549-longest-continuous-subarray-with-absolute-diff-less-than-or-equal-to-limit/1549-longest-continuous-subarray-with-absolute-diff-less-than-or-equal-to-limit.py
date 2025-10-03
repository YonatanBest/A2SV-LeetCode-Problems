class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_stack = deque()
        min_stack = deque()
        i = 0
        j = 0
        max_len = 0
        while j < len(nums):
            while max_stack and max_stack[-1] < nums[j]:
                max_stack.pop()
            while min_stack and min_stack[-1] > nums[j]:
                min_stack.pop()
            max_stack.append(nums[j])
            min_stack.append(nums[j])
            while max_stack and min_stack and max_stack[0] - min_stack[0] > limit:
                if max_stack[0] == nums[i]:
                    max_stack.popleft()
                if min_stack[0] == nums[i]:
                    min_stack.popleft()
                i += 1
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len