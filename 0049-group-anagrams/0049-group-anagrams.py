class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            x = i
            if "".join(sorted(list(x))) in dic:
                dic["".join(sorted(list(x)))].append(i)
            else:
                dic["".join(sorted(list(x)))] = [i]
        arr = []
        for j in dic:
            arr.append(dic[j])
        return arr
