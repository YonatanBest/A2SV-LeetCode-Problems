# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp1 = l1
        temp2 = l2
        num1 = []
        num2 = []
        while temp1 and temp2:
            num1.append(temp1.val)
            num2.append(temp2.val)
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1:
            num1.append(temp1.val)
            temp1 = temp1.next
        while temp2:
            num2.append(temp2.val)
            temp2 = temp2.next
        j = 0
        temp = 0
        ans = []
        while j < len(num1) and j < len(num2):
            ans.append((num1[j] + num2[j] + temp)%10)
            maybe = temp
            temp = 0
            if num1[j] + num2[j] + maybe> 9:
                temp += (num1[j] + num2[j] + maybe)//10
            j += 1
        while j < len(num1):
            ans.append((num1[j] + temp)%10)
            maybe = temp
            temp = 0
            if num1[j] + maybe> 9:
                temp += (num1[j] + maybe)//10
            j += 1
        while j < len(num2):
            ans.append((num2[j] + temp)%10)
            maybe = temp
            temp = 0
            if num2[j] + maybe > 9:
                temp += (num2[j] + maybe)//10
            j += 1
        if temp != 0:
            ans.append(temp)
        print(ans)
        dummy = ListNode()
        current = dummy
        for i in ans:
            new_node = ListNode()
            new_node.val = i
            current.next = new_node
            current = current.next
        return dummy.next
            