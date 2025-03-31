# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        def linked(current):
            if not current:
                return dummy.next
            if current and current.next and current.next.val == val:
                current.next = current.next.next
                linked(current)
            linked(current.next)
            return dummy.next
        return linked(dummy)