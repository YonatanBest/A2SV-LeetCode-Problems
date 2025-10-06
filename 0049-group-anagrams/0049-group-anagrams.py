class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for j in strs:
            anagrams["".join(sorted(j))].append(j)
        return list(anagrams.values())