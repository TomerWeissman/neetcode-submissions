# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def verify(node, subnode):
            if not node and not subnode:
                return True
            
            if (not node and subnode or
                not subnode and node or
                node.val != subnode.val
                ):
                return False
            
            if not verify(node.left, subnode.left):
                return False
            
            if not verify(node.right, subnode.right):
                return False
            
            return True
        
        def dfs(node):
            
            if not node:
                return False
            
            if verify(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

            


        