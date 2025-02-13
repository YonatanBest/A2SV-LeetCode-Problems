# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = 0
        i = 0
        j = 0
        dic = {}
        while j < len(s):
            if s[j] not in dic:
                dic[s[j]] = 1
            else:
                while s[j] in dic:
                    dic[s[i]] -= 1
                    if dic[s[i]] == 0:
                        del dic[s[i]]
                    i += 1
                dic[s[j]] = 1
            max_substring = max(max_substring, len(dic))
            j += 1
        return max_substring