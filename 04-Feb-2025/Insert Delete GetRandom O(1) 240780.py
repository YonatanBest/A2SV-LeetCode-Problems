# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

import random
class RandomizedSet:
    
    def __init__(self):
        self.index_map = {}
        self.list_elements = []

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.index_map[val] = len(self.list_elements)
            self.list_elements.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            self.list_elements[self.index_map[val]], self.list_elements[-1] = self.list_elements[-1], self.list_elements[self.index_map[val]]
            self.index_map[self.list_elements[self.index_map[val]]], self.index_map[val] = self.index_map[val], self.index_map[self.list_elements[self.index_map[val]]]
            del self.index_map[self.list_elements.pop()]
            return True
        return False

    def getRandom(self) -> int:
        rand_index = randint(0, len(self.list_elements) - 1)
        return self.list_elements[rand_index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()