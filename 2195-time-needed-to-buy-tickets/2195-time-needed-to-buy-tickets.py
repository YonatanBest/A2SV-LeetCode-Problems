class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0
        while tickets[k] != 0:
            for i in range(len(tickets)):   
                if tickets[i] != 0:
                    tickets[i] -= 1
                    cnt += 1
                if i == k and tickets[k] == 0:
                    return cnt

