class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        output = []

        for i in range(len(nums)):
            if target - nums[i] in hashmap.keys():
                return [hashmap[target - nums[i]], i]
            
            hashmap[nums[i]] = i
