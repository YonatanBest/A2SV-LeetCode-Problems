class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5:0, 10:0, 20:0}
        for i in bills:
            if i == 20:
                if changes[10] > 0 and changes[5] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] > 2:
                    changes[5] -= 3
                else:
                    return False
            elif i == 10:
                if changes[5] > 0:
                    changes[5] -= 1
                else:
                    return False
            changes[i] += 1
        return True