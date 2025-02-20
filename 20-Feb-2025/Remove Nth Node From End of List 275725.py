# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        length = -1
        while current:
            current = current.next
            length += 1
        length -= n - 1

        current = dummy
        for i in range(length - 1):
            current = current.next
        current.next = current.next.next
        return dummy.next