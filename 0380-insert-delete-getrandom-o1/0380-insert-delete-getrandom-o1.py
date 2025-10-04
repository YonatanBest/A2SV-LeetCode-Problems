class RandomizedSet:

    def __init__(self):
        self.dic = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dic:
            del self.dic[val]
            return True
        return False

    def getRandom(self) -> int:
        index = random.choice(list(self.dic.values()))
        return self.arr[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()