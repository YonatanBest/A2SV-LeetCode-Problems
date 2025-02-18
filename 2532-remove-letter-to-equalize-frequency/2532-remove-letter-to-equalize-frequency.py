class Solution:
    def equalFrequency(self, word: str) -> bool:
        test = list(set(word))
        dic_temp = Counter(word)
        check = True
        dic = copy.deepcopy(dic_temp)
        for i in test:
            check = True
            dic[i] -= 1
            if dic[i] == 0:
                del dic[i]
            flag = True
            for j in dic:
                if flag:
                    flag = False
                    temp = dic[j]
                if dic[j] != temp:
                    check = False
                    break
            if check:
                return check
            dic = copy.deepcopy(dic_temp)
        return check