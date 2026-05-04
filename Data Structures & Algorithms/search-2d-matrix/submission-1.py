class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        new_lst = []
        for lst in matrix:
            new_lst += lst

        l = 0
        r = len(new_lst) - 1

        while l <= r:
            m = (l+r)//2
        
            if new_lst[m] > target:
                r = m - 1
            elif new_lst[m] < target:
                l = m + 1
            else:
                return True
        
        return False

        

        