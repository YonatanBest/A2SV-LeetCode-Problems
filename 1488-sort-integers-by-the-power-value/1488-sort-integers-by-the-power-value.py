class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memorization = defaultdict(int)
        sort_int = []

        def power_finder(num):

            if num in memorization:
                return memorization[num]

            if num == 1:
                return 0

            if num % 2:
                new = 3 * num + 1
            else:
                new = num // 2

            count = 1 + power_finder(new)

            memorization[num] = count

            return count

        for j in range(lo, hi + 1):
            sort_int.append([j, power_finder(j)])

        sort_int.sort(key=lambda x: x[1])

        return sort_int[k - 1][0]