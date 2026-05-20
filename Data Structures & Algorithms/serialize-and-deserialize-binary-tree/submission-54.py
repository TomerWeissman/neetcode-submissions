# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        self.res = ''
        def dfs(node):

            if not node:
                self.res += 'N,'
                return
            
            self.res += str(node.val) + ','
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        data = data.split(',')
        self.i = 0

        def createTree():

            if data[self.i] == 'N':
                self.i += 1
                return None
            
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = createTree()
            root.right = createTree()
            return root
        
        return createTree()
