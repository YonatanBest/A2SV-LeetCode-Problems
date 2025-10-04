class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(path, dic):
            if len(path) == n * 2:
                if dic["("] == dic[")"]:
                    ans.append("".join(path.copy()))
                return
            for j in ["(", ")"]:
                dic[j] += 1
                if dic[")"] > dic["("]:
                    dic[j] -= 1
                    continue
                path.append(j)
                backtrack(path, dic)
                dic[j] -= 1
                path.pop()
            return
        backtrack([], defaultdict(int))
        return ans