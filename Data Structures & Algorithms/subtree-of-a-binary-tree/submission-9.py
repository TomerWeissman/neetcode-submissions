# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def check_tree(n1, n2):

            if not n1 and not n2:
                return True
            
            if (
                not n1 and n2 or 
                not n2 and n1 or
                n1.val != n2.val
                ):
                return False
            
            if not check_tree(n1.left, n2.left):
                return False
            
            if not check_tree(n1.right, n2.right):
                return False
            
            return True
        
        def traverse(node):

            if not node:
                return False
            
            if node.val == subRoot.val:
                if check_tree(node, subRoot):
                    return True
            
            if traverse(node.left):
                return True
            if traverse(node.right):
                return True
            
            return False
        
        return traverse(root)

            

        