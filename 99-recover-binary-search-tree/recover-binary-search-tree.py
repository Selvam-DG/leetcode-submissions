# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        curr = root
        prev = None
        first = None
        second = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and prev.val > curr.val:
                if first is None:
                    first = prev
                second = curr
            prev = curr
            curr = curr.right
        
        first.val, second.val = second.val, first.val
        