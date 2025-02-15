class Solution:
    def validPalindrome(self, s: str) -> bool:
        letter = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
        check = False
        count = float("inf")
        for l in range(26):
            i = 0
            j = len(s) - 1
            temp = 0
            while i < j:
                
                if s[i] != s[j]:
                    temp += 1
                    if s[i] == letter[l]:
                        i += 1
                    elif s[j] == letter[l]:
                        j -= 1
                    else:
                        temp = None
                        break
                else:
                    i += 1
                    j -= 1
            if temp != None:
                count = min(count, temp)
       
        if count == 1 or count == 0:
            check = True

        return check