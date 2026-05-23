# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        #3 variables
        #1 - Left path + node
        #2 - right path + node
        #3 - left + right + node

        #edge cases
        if not root:
            return None

        #store variables (maxRes)
        self.maxRes = float('-inf')

        #create dfs
        def dfs(node):

            if not node:
                return 0

            #left ->
            #right ->

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            print(left)
            print(right)

            #if left + right + node > maxRes
            #maxRes = ...
            self.maxRes = max(left+right+node.val, self.maxRes)

            #return max(left, right)
            return node.val + max(left, right)

        #run dfs
        dfs(root)
        #return maxRes
        return self.maxRes
        