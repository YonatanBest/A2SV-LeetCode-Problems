# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        while current:
            tail = current
            count += 1
            current = current.next
        dummy = ListNode()
        dummy.next = head
        current = dummy
        index = 1
        while count:
            temp = current
            current = current.next
            if index % 2 == 0:
                new_node = ListNode()
                new_node.val = current.val
                tail.next = new_node
                tail = new_node
                temp.next = temp.next.next
            index += 1
            count -= 1
        return dummy.next