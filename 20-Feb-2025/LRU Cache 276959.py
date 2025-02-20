# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        self.key = None

    def __str__(self):
        arr = [self.val]
        curr = self.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        return ', '.join(map(str, arr))

class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = Node()
        self.tail = self.LRU
        self.count = 0
        self.length = capacity
        self.dic = {}

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        temp = node.val
        self.put(key, node.val)
        return temp

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            if node == self.tail:
                node.val = value
            else:
                new_node = Node(value)
                new_node.key = key
                self.tail.next = new_node
                self.tail = self.tail.next
                self.dic[key] = new_node
                node.val = node.next.val
                node.key = node.next.key
                node.next = node.next.next
                self.dic[node.key] = node
        else:
            new_node = Node(value)
            new_node.key = key
            self.tail.next = new_node
            self.tail = self.tail.next
            self.dic[key] = new_node
            self.count += 1
        
        if self.count > self.length:
            del self.dic[self.LRU.next.key]
            self.LRU.next = self.LRU.next.next
            self.count -= 1
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)