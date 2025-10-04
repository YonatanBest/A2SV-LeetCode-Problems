# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        noder = ListNode()
        carry = 0
        node = noder
        while l1 and l2:
            num = l1.val + l2.val + carry
            node.next = ListNode(num%10)
            node = node.next
            carry = num // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            num = l1.val + carry
            node.next = ListNode(num%10)
            node = node.next
            carry = num // 10
            l1 = l1.next
        while l2:
            num = l2.val + carry
            node.next = ListNode(num%10)
            node = node.next
            carry = num // 10
            l2 = l2.next
        while carry:
            node.next = ListNode(carry%10)
            node = node.next
            carry //= 10
        return noder.next