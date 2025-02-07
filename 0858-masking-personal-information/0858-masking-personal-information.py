class Solution:
    def maskPII(self, s: str) -> str:
        name_final = ""
        if s[0].isalpha():
            name, domain = s.split("@")
            name_final += name[0].lower()
            name_final += "*****"
            name_final += name[-1].lower()
            name_final += "@"
            name_final += domain.lower()
        else:
            number = ""
            for i in s:
                if i.isalnum():
                    number += i
            if len(number) == 10:
                name_final = "***-***-"
                name_final += number[6:10]
            else:
                name_final = "+"
                for i in range(len(number) - 10):
                    name_final += "*"
                name_final += "-***-***-"
                name_final += number[len(number) - 4:len(number)]
        return name_final
        