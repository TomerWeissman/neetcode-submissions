"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        visit = set()
        hashmap = {}

        def traverse(root):

            if not root:
                return None

            if root in visit:
                return hashmap[root]
            
            visit.add(root)
            new_node = Node(root.val)
            hashmap[root] = new_node

            for neighbor in root.neighbors:
                if neighbor:
                    new_node.neighbors.append(traverse(neighbor))
            
            return new_node
        
        return traverse(node)