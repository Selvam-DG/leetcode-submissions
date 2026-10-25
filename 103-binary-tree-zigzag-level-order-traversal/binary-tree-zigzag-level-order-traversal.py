# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []

        queue = deque()
        if not root:
            return result
        queue.append(root)
        is_left_right = True

        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if  not is_left_right:
                temp.reverse()
            result.append(temp)
            
            is_left_right = not is_left_right
        
        return result