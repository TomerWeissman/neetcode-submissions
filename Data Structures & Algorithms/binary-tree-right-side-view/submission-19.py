# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        res = []
        queue = deque()
        queue.append(root)

        if not root:
            return []

        while queue:

            length = len(queue)
            for i in range(length):
                curr = queue.popleft()

                if i == length - 1 and curr:
                    res.append(curr.val)

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                
        return res
        