# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val = 0, next = None):
        self.next = next
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.tail = None
        self.length = 0
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        else:
            curr_index = 0
            current = self.dummy.next
            while curr_index < index:
                current = current.next
                curr_index += 1
            return current.val
    def addAtHead(self, val: int) -> None:
        head = self.dummy.next
        new_node = Node(val)
        self.dummy.next = new_node
        new_node.next = head
        self.length += 1
        if not self.tail:
            self.tail = new_node
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.dummy.next = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
        else:
            curr_index = 0
            current = self.dummy
            while curr_index < index:
                current = current.next
                curr_index += 1

            new_node = Node(val)
            new_node.next = current.next
            current.next = new_node
            self.length += 1
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        else:
            curr_index = 0
            current = self.dummy
            while curr_index < index:
                current = current.next
                curr_index += 1
            current.next = current.next.next
            if not current.next:
                self.tail = current
            self.length -= 1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)