class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > 1:
                return True
    

        return False

        