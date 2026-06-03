"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None
        
        queue = deque([root])


        while queue:

            length = len(queue)
            for i in range(length):

                curr = queue.popleft()

                if i == length - 1:
                    curr.next = None
                else:
                    curr.next = queue[0]
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
        return root






'''
Breadth first search


'''
        