from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        res = []
        for i in cpdomains:
            num, domain = i.split()
            num = int(num)
            arr = domain.split(".")
            test = ""
            for j in range(len(arr)):
                test = ".".join(arr[j:len(arr)+1])
                dic[test] += num
        for k in dic:
            res.append(" ".join([str(dic[k]), k]))
        return res