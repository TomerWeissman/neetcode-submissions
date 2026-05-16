class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        l1 = 0
        r1 = l - 1
        l2 = l
        r2 = len(nums) - 1

        print('---')
        print(f'{l1} {l2} {r1} {r2}')
        print('---')

        def binary(left, right):
            while left <= right:
                print(nums[left])
                print(nums[right])
                mid = (left + right)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
            return -1
        
        ans_l = binary(l1, l2)
        ans_r = binary(l2, r2)

        if ans_l >= 0:
            return ans_l
        elif ans_r >= 0:
            return ans_r
        
        return -1



        