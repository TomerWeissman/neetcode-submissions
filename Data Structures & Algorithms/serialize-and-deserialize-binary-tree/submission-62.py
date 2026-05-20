# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []
        def preorder(node):

            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        data = data.split(',')
        self.i = 0

        def createTree():
            if self.i > len(data) - 1:
                return
            
            if data[self.i] == 'N':
                self.i += 1
                return
            
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = createTree()
            node.right = createTree()
            return node
        
        return createTree()
