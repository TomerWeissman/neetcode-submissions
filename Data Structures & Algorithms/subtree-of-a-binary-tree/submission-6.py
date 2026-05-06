# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def preorder(arr, node):
            if not node:
                arr.append(None)
                return None
            
            arr.append(node.val)
            preorder(arr, node.left)
            preorder(arr, node.right)

        if not root:
            return False

        if root.val == subRoot.val:
            tree_arr = []
            sub_arr = []

            preorder(tree_arr, root)
            preorder(sub_arr, subRoot)

            if tree_arr == sub_arr:
                return True
        
        if self.isSubtree(root.right, subRoot):
            return True
        
        if self.isSubtree(root.left, subRoot):
            return True
        
        return False



        