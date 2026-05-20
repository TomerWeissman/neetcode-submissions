# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        def traverse(node):

            if len(res) >= k:
                return
            
            if not node:
                return
            
            traverse(node.left)
            res.append(node)
            traverse(node.right)
            return node
        
        traverse(root)
        return res[k-1].val