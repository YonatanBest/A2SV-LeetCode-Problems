class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        ans = []
        for j in strs:
            dic["".join(sorted(j))].append(j)
        return list(dic.values())