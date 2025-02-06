class Solution:
    def intToRoman(self, num: int) -> str:
        # dic = {1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M"}
        ans = ""
        temp = num
        h = 10**(len(str(num)) - 1)
        num = (num // h)*h
        while num > 0:
            if num >= 1000:
                mod = num // 1000
                for i in range(mod):
                    ans += "M"
            elif num == 900:
                ans += "CM"
            elif num >= 500:
                mod = (num - 500)//100
                ans += "D"
                for i in range(mod):
                    ans += "C"
            elif num == 400:
                ans += "CD"
            elif num >= 100:
                mod = num // 100
                for i in range(mod):
                    ans += "C" 
            elif num == 90:
                ans += "XC"
            elif num >= 50:
                mod = (num - 50)//10
                ans += "L"
                for i in range(mod):
                    ans += "X"
            elif num >= 40:
                mod = (50 - num)//10
                for i in range(mod):
                    ans += "X"
                ans += "L"
            elif num >= 10:
                mod = num // 10
                for i in range(mod):
                    ans += "X"
            elif num >= 9:
                mod = num - 8
                for i in range(mod):
                    ans += "I"
                ans += "X"
            elif num >= 5:
                mod = num - 5
                ans += "V"
                for i in range(mod):
                    ans += "I"
            elif num == 4:
                ans += "IV"
            else:
                for i in range(num):
                    ans += "I"
            print(num)
            print(ans)
            temp -= num
            num = temp
            h = 10**(len(str(num)) - 1)
            num = (num // h)*h
        return ans
            