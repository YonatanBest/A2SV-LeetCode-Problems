class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stemp = {}
        ttemp = {}
        sans = []
        tans = []
        for x in range(len(s)):
            
            if s[x] in stemp:
                sans.append(str(stemp[s[x]]))
            else:
                stemp[s[x]] = len(stemp)
                sans.append(str(stemp[s[x]]))

            if t[x] in ttemp:
                tans.append(str(ttemp[t[x]]))
            else:
                ttemp[t[x]] = len(ttemp)
                tans.append(str(ttemp[t[x]]))
        return sans == tans