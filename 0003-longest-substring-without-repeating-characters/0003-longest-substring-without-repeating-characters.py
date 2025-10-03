class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        i = 0
        j = 0
        max_len = 0
        while j < len(s):
            dic[s[j]] += 1
            while len(dic) != j - i + 1:
                dic[s[i]] -= 1
                if dic[s[i]] == 0:
                    del dic[s[i]]
                i += 1
            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len