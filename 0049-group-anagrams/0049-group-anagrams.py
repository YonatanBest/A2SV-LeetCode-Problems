class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        ans = []
        for j in strs:
            dic["".join(sorted(list(j)))].append(j)
        for j in dic:
            ans.append(dic[j])
        return ans