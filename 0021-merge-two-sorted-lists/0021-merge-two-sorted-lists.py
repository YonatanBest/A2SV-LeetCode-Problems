# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        current1 = list1
        current2 = list2
        while current1 and current2:
            if current1.val > current2.val:
                current.next = current2
                current2 = current2.next
            else:
                current.next = current1
                current1 = current1.next
            current = current.next
        while current2:
            current.next = current2
            current2 = current2.next
            current = current.next
        while current1:
            current.next = current1
            current1 = current1.next
            current = current.next
        return dummy.next