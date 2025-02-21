# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        test = True
        while test:
            test = False
            check = defaultdict(int)
            current = dummy
            while current and current.next:
                temp = current
                current = current.next
                if current.val in check:
                    temp.next = temp.next.next
                    check[current.val] -= 1
                    test = True
                check[current.val] += 1
        return dummy.next