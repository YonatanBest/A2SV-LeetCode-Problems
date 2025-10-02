class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.queue = deque()
        self.k = k
        self.dic = defaultdict(int)
    def consec(self, num: int) -> bool:
        if num != self.value:
            self.dic[num] += 1
        self.queue.append(num)
        if len(self.queue) < self.k:
            return False
        if len(self.queue) > self.k:
            temp = self.queue.popleft()
            if temp in self.dic:
                self.dic[temp] -= 1
                if self.dic[temp] == 0:
                    del self.dic[temp]
        return not self.dic

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)