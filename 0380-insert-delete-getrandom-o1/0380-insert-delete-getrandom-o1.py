import random
class RandomizedSet:
    
    def __init__(self):
        self.x = set()

    def insert(self, val: int) -> bool:
        if val not in self.x:
            self.x.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.x:
            self.x.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if len(self.x) > 0:
            return list(self.x)[random.randint(0, len(self.x) - 1)]
        else:
            return []

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()