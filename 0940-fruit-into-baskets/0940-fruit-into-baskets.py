from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        basket = defaultdict(int)
        max_len = 0
        while j < len(fruits):
            if fruits[j] not in basket:
                while len(basket) == 2:
                    basket[fruits[i]] -= 1
                    if basket[fruits[i]] == 0:
                        del basket[fruits[i]]
                    i += 1
            basket[fruits[j]] += 1
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len
