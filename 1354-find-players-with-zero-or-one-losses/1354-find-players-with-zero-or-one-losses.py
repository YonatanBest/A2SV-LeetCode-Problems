class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnersall = []
        losersonce = []
        winners = set()
        losers = {}
        for w, l in matches:
            winners.add(w)
            if l in losers:
                losers[l] += 1
            else:
                losers[l] = 1
        
        for i in winners:
            if i not in losers:
                winnersall.append(i)
        for i in losers:
            if losers[i] == 1:
                losersonce.append(i)
        return [sorted(winnersall), sorted(losersonce)]
        
