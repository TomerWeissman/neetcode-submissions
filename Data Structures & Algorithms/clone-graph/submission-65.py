"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #init visit
        visit = set()

        node_map = {}

        #dfs
        def dfs(node):

            #bascases: node in visit
            if node in visit:
                return node_map[node]
            
            if not node:
                return None

            new_node = Node(node.val)
            node_map[node] = new_node

            #add node to visit
            visit.add(node)

            for nei in node.neighbors:

                #add dfs(nei) to neighbors
                new_nei = dfs(nei)
                if new_nei:
                    new_node.neighbors.append(new_nei)
            
            return new_node


        return dfs(node)      