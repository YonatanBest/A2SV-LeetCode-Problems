class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        test = []
        for i in nums2:
            while test and test[-1] < i:
                ans[test.pop()] = i
            test.append(i)
        test = []
        for i in nums1:
            if i in ans:
                test.append(ans[i])
            else:
                test.append(-1)
        return test