class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(nums1)):
            dic[nums1[i]] = i
        ans = defaultdict(int)
        stack = []
        for j in nums2:
            ans[j] = -1
            if not stack:
                stack.append(j)
            while stack and stack[-1] < j:
                ans[stack.pop()] = j
            stack.append(j)
        for k in dic:
            nums1[dic[k]] = ans[k]
        return nums1