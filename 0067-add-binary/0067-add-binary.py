class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(reversed(a))
        b = list(reversed(b))
        ans = []
        carry = False
        j = 0
        while j < len(a) and j < len(b):
            if a[j] == "1" and b[j] == "1":
                if carry:
                    ans.append("1")
                else:
                    ans.append("0")
                carry = True
            elif a[j] != b[j]:
                if carry:
                    ans.append("0")
                else:
                    ans.append("1")
            elif carry:
                carry = False
                ans.append("1")
            else:
                ans.append("0")
            j += 1

        while j < len(a):
            if a[j] == "0" and carry:
                carry = False
                ans.append("1")
            elif carry:
                ans.append("0")
            else:
                ans.append(a[j])
            j += 1

        while j < len(b):
            if b[j] == "0" and carry:
                carry = False
                ans.append("1")
            elif carry:
                ans.append("0")
            else:
                ans.append(b[j])
            j += 1

        if carry:
            ans.append("1")
        
        return "".join(list(reversed(ans)))
        
        