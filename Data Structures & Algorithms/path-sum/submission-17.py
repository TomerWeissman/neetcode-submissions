# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root:
            targetSum -= root.val
        else:
            return False
        
        if not root.right and not root.left:
            if targetSum == 0:
                return True
            
        if self.hasPathSum(root.right, targetSum):
            return True
        
        if self.hasPathSum(root.left, targetSum):
            return True
        
        targetSum += root.val
        return False



            
            

            
        