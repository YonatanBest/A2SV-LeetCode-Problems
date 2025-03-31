# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def linked(current):
            if not current:
                return None
            if current.next == None:
                if current.val == val:
                    return None
                else:
                    return current
            if current.val != val:
                current.next = linked(current.next)
            else:
                return linked(current.next)
            return current
        return linked(head)