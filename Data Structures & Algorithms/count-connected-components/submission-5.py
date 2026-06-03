class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_dict = {}

        for i in range(n):
            adj_dict[i] = []
        
        for edge in edges:
            first, second = edge

            adj_dict[first].append(second)
            adj_dict[second].append(first)
        
        visit = set()
        def dfs(node):

            if node in visit or adj_dict[node] == []:
                return
            
            visit.add(node)
            for next_node in adj_dict[node]:
                dfs(next_node)
        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        
        return count






'''
1. create a adj list

2. create a dfs

    if no next, stop

    if in visit, stop

    add to visit

    for i in next:

            dfs(i)

3. run through; 
    if not in visit:
        run
        += 1 count


'''
        