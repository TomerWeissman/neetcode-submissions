class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_min(arr):
            l = 0
            r = len(arr) - 1

            while l < r:
                m = (l+r)//2

                if arr[m] < arr[r]:
                    r = m
                elif arr[m] > arr[r]:
                    l = m + 1
            
            return r
        
        def search_t(arr, t, l, r):

            while l <= r:
                m = (l + r)//2

                if arr[m] > t:
                    r = m - 1
                elif arr[m] < t:
                    l = m + 1
                else:
                    return m
            
            return -1

        min_ind = find_min(nums)

        right = search_t(nums, target, min_ind, len(nums) - 1)

        if right > -1:
            return right
        else:
            return search_t(nums, target, 0, min_ind - 1)







                
            



        