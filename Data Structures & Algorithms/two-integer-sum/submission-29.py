class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(list)

        for i, num in enumerate(nums):
            hashmap[num].append(i)

            if (target - num) in hashmap:
                if len(hashmap[target - num]) > 1:
                    return hashmap[target - num]
                elif hashmap[target - num] != [i]:
                    return [hashmap[target - num][0], i]
        

        return None
        


        