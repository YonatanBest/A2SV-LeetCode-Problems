class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = None
        ans = 0
        i = 0
        j = len(skill) - 1
        while i < j:
            if n == None:
                n = skill[i] + skill[j]
            elif n != skill[i] + skill[j]:
                return -1
            ans += skill[i] * skill[j]
            i += 1
            j -= 1
        return ans