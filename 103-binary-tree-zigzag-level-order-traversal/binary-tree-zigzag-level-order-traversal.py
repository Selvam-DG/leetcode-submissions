# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []
        if not root:
            return result

        q.append(root) 
        left_to_right = True

        while q:
            level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            result.append(list(level))
            left_to_right = not left_to_right
        
        return result
        
        return result
        