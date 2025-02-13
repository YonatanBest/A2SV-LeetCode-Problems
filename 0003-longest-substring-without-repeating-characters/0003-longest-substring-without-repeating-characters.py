class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = 0
        i = 0
        j = 0
        dic = set()
        while j < len(s):
            if s[j] not in dic:
                dic.add(s[j])
            else:
                while s[j] in dic:
                    dic.remove(s[i])
                    i += 1
                dic.add(s[j])
            max_substring = max(max_substring, len(dic))
            j += 1
        return max_substring