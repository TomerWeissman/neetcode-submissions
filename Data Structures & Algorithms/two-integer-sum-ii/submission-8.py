class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            
            elif numbers[l] + numbers[r] < target:
                l += 1
                while numbers[l] == numbers[l+1] and l < r:
                    l += 1
            
            else:
                r -= 1
                while numbers[r] == numbers[r-1] and l < r:
                    r -= 1
        

            
        