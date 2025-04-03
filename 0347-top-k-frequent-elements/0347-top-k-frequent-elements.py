class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        max_occur = 0
        for i in nums:
            dic[i] += 1
            max_occur = max(max_occur, dic[i])
        bucket = [[] for i in range(max_occur + 1)]

        for i in dic:
            bucket[dic[i]].append(i)
        ans = []
        for j in range(len(bucket) - 1, -1, -1):
            ans.extend(bucket[j])
            if len(ans) >= k:
                return ans
        return ans