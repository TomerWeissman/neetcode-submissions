# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        #self.ans = ...
        self.ans = []
        
        #preorder function
        def preorder(node):

            if not node:
                self.ans.append('N')
                return

            #self.ans.append(node.val)
            self.ans.append(str(node.val))

            #left preorder
            preorder(node.left)

            #right preorder
            preorder(node.right)
        
        preorder(root)
        print(','.join(self.ans))
        return ','.join(self.ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        #self.i = 0
        self.i = 0
        
        data = data.split(',')

        def createTree(data):

            #base case
            if self.i > len(data) - 1:
                return None
            
            if data[self.i] == 'N':
                return None

            #node = TreeNode(data[self.i])
            node = TreeNode(data[self.i])
            
            self.i += 1
            node.left = createTree(data)
            
            self.i += 1
            node.right = createTree(data)

            return node
        
        return createTree(data)


