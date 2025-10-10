# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverser(curr, queue):
            if not curr:
                return
            if not curr.next:
                queue.append(curr.val)
                curr.val = queue.popleft()
                return
            queue.append(curr.val)
            reverser(curr.next, queue)
            curr.val = queue.popleft()

            return
        
        reverser(head, deque())
        return head