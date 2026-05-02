class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        num_set = set(nums)

        for num in nums:
            if num - 1 not in num_set:
                curr = 1
                while num + 1 in num_set:
                    curr += 1
                    num += 1
                maxlen = max(curr, maxlen)
        
        return maxlen


        