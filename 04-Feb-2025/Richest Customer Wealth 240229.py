# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for i in accounts:
            rich = max(rich, sum(i))
        return rich