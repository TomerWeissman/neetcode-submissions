# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(arr, node):
            if not node:
                arr.append(None)
                return
            
            arr.append(node.val)
            dfs(arr, node.left)
            dfs(arr, node.right)

        
        arr_p = []
        arr_q = []

        dfs(arr_p, p)
        dfs(arr_q, q)

        print(arr_p)
        print(arr_q)

        if arr_p == arr_q:
            return True
        
        return False


        