# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        max_sum = float("-inf")
        i = 0
        j = len(arr) - 1
        while i < j:
            max_sum = max(max_sum, arr[i] + arr[j])
            i += 1
            j -= 1

        return max_sum