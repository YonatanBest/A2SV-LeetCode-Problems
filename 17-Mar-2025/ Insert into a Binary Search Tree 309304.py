# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        new_node = TreeNode()
        new_node.val = val
        while current:
            temp = current
            if current.val > val:
                current = current.left
            else:
                current = current.right
        if not root:
            root = new_node
        else:
            if temp.val > val:
                temp.left = new_node
            else:
                temp.right = new_node
        return root
        