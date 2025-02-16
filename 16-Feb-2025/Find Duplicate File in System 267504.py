# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        
        for path in paths:
            dirr, *files = path.split()

            for f in files:
                fname, fcont = f.split('(')
                my_dict[list(fcont.split(")"))[0]].append(dirr + "/" + fname)
        arr = []
        for i in my_dict:
            if len(my_dict[i]) > 1:
                arr.append(my_dict[i])
        return arr