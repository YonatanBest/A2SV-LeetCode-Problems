class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        new = []
        for k in s:
            if k != " ":
                new.append(k)
            else:
                arr.extend(reversed(new))
                arr.append(" ")
                new = []
        arr.extend(reversed(new))
        return "".join(arr)