class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = [s[0]]  
        for x in range(1, len(s) - 1):
            mid = x
            i = mid - 1
            j = mid + 1
            string = deque([s[mid]])
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                string.appendleft(s[i])
                string.append(s[j])
                i -= 1
                j += 1

            if len(max_str) < len(string):
                max_str = string.copy()

        for x in range(0, len(s) - 1):
            if x + 1 >= len(s) or s[x] != s[x + 1]:
                continue
            i = x
            j = x + 1
            string = deque([s[i], s[j]])
            i -= 1
            j += 1
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                string.appendleft(s[i])
                string.append(s[j])
                i -= 1
                j += 1

            if len(max_str) < len(string):
                max_str = string.copy()

        return "".join(max_str)