class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        cnt = 0
        test = -1
        while i < len(haystack):
            if haystack[i] == needle[j]:
                cnt += 1
                j += 1
            else:
                test += 1
                i = test
                cnt = 0
                j = 0
            if cnt == len(needle):
                return i - len(needle) + 1
            i += 1
        return -1