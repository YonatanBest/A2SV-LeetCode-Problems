class UndergroundSystem:

    def __init__(self):
        self.checks = defaultdict(list[int, str])
        self.location_time = defaultdict(list[int, int])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checks[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.checks[id][1], stationName) in self.location_time:
            self.location_time[(self.checks[id][1], stationName)][0] += (t - self.checks[id][0])
            self.location_time[(self.checks[id][1], stationName)][1] += 1
        else:
            self.location_time[(self.checks[id][1], stationName)] = [(t - self.checks[id][0]), 1]
        del self.checks[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.location_time[(startStation, endStation)][0] / self.location_time[(startStation, endStation)][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)