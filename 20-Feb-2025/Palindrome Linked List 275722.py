# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        original_node = copy.deepcopy(head)
        dummy = None
        current = head
        while current:
            temp = current.next
            current.next = dummy
            dummy = current
            current = temp
        while dummy and original_node:
            if dummy.val != original_node.val:
                return False
            dummy = dummy.next
            original_node = original_node.next
        return True