# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        def reverser(curr, level):
            if not curr:
                return
            if not curr.next:
                arr.append(curr.val)
                curr.val = arr[0]
                return
            arr.append(curr.val)
            reverser(curr.next, level + 1)
            curr.val = arr[len(arr) - level]

            return
        
        reverser(head, 1)
        return head