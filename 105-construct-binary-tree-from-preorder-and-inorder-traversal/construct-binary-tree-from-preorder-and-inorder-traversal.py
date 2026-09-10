# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {num:i for i,num in enumerate(inorder)}
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        pre_idx = 0
        def build(low, high):
            nonlocal pre_idx
            if low > high:
                return None

            node_val = preorder[pre_idx]
            pre_idx += 1
            node = TreeNode(node_val)

            split = inorder_idx[node_val]

            node.left = build(low, split-1)
            node.right = build(split+1, high)

            return node
        
        root = build(0, len(preorder)-1)
        return root
