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
        visit = set() #O(1)

        node_map = {} #O(1)

        #dfs
        def dfs(node):

            #bascases: node in visit
            if node in visit: #O(1)
                return node_map[node]
            
            if not node: #O(1)
                return None

            new_node = Node(node.val) #O(1)
            node_map[node] = new_node #O(1)

            #add node to visit
            visit.add(node) #O(1)

            for nei in node.neighbors: #O(n)

                #add dfs(nei) to neighbors
                new_nei = dfs(nei) #O(n)
                if new_nei: #O(1)
                    new_node.neighbors.append(new_nei)
            
            return new_node


        return dfs(node)  #O(n^2)    