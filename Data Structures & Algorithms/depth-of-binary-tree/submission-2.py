# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(curr, node):

            if not node:
                return curr
            
            curr = max(1+dfs(curr, node.left), 1+dfs(curr, node.right))

            return curr
        
        return dfs(0, root)
        



            
            



        