class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        reminder = 0
        while numBottles > 0:
            ans += numBottles
            temp = numBottles + reminder
            numBottles = (numBottles + reminder) // numExchange
            reminder = temp % numExchange
        return ans
