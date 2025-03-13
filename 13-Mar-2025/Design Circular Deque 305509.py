# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self):
        arr = []
        curr = self
        while curr:
            arr.append(str(curr.val))
            arr.append('->')
            curr = curr.next
        return ''.join(arr)
class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = Node()
        self.max_len = k
        self.count = 0
        self.tail = Node()
        self.queue.next = self.tail
        self.tail.prev = self.queue

    def insertFront(self, value: int) -> bool:
        print("if", self.queue)
        if self.count == self.max_len:
            return False
        new_node = Node()
        new_node.val = value
        new_node.prev = self.queue
        new_node.next = self.queue.next
        self.queue.next.prev = new_node
        self.queue.next = new_node
        self.count += 1
        print('if', self.queue, self.tail)
        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.max_len:
            return False
        new_node = Node()
        new_node.val = value
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        print('il', self.queue, self.tail)
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if not self.count:
            return False
        self.queue.next.next.prev = self.queue
        self.queue.next = self.queue.next.next
        self.count -= 1
        print('df', self.queue)
        return True

    def deleteLast(self) -> bool:
        print('dl', self.queue, self.tail, self.tail.prev)
        if not self.count:
            return False
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.count -= 1
        print('dl', self.queue)
        return True
        # 0 4x
    def getFront(self) -> int:
        if not self.count:
            return -1
        print('gf', self.queue)
        return self.queue.next.val

    # 0 6 

    def getRear(self) -> int:
        if not self.count:
            return -1
        print('gr', self.queue)
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        if self.count:
            return False
        return True

    def isFull(self) -> bool:
        if self.count == self.max_len:
            return True 
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()