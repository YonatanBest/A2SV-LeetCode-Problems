class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = Counter(answers)
        count = 0
        for i in dic:
            temp = 0
            temp += (i + 1)*(dic[i] // (i+1))
            if dic[i] % (i + 1):
                temp += i + 1
            count += temp
        print(count)
        return count