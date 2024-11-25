class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = {}
        dic2 = {}
        for i in nums1:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        for j in nums2:
            if j in dic2:
                dic2[j] += 1
            else:
                dic2[j] = 1
        ans = []
        for k in dic1:
            if k in dic2:
                for l in range(min(dic1[k], dic2[k])):
                    ans.append(k)
        return ans