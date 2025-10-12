# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def reverser(curr):

            if not curr.next:
                return [curr, curr]

            temp, take = reverser(curr.next)
            curr.next = None
            take.next = curr

            return [temp, take.next]
        
        return reverser(head)[0]