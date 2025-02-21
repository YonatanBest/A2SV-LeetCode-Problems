# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        new = ListNode()
        test = new
        current = dummy
        while current and current.next:
            tail = current
            temp = current
            current = current.next
            if current.val >= x:
                test.next = ListNode(current.val)
                test = test.next
                temp.next = temp.next.next
                current = tail
        current = dummy
        while current:
            tail = current
            current = current.next
        tail.next = new.next
        return dummy.next
