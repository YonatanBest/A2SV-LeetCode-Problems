class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = []
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or strs[0][i] != word[i]:
                    return "".join(longest_common_prefix)
            longest_common_prefix.append(word[i])
        return "".join(longest_common_prefix)
                