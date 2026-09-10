# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        node = root
        visited = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            visited += 1
            if visited == k:
                return node.val
            
            node = node.right

        return -1