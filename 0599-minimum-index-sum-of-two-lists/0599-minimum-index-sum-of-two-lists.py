class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {}
        dic2 = {}
        for i in range(len(list1)):
            if list1[i] in dic1:
                dic1[list1[i]].append(i)
            else:
                dic1[list1[i]] = [i]
        for j in range(len(list2)):
            if list2[j] in dic2:
                dic2[list2[j]].append(j)
            else:
                dic2[list2[j]] = [j]
        arr = []
        res = float('inf')
        for k in dic1:
            if k in dic2:
                if dic1[k][0] + dic2[k][0] < res:
                    arr = [k]
                    res = dic1[k][0] + dic2[k][0]
                elif dic1[k][0] + dic2[k][0] == res:
                    arr.append(k)
        return arr