class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        vaild_str = []
        stack = []
        for j in range(len(s)):
            if s[j] != "(" and s[j] != ")":
                vaild_str.append(s[j])
            elif s[j] == "(":
                vaild_str.append("")
                stack.append(j)  
            elif stack and s[j] == ")":
                vaild_str[stack.pop()] = "("
                vaild_str.append(")")
            else:
                vaild_str.append("")


        
        return "".join(vaild_str)
                

        
        
        