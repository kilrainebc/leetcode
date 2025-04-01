class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### Brute Force Solution: check every combination
        # for idx, num in enumerate(nums):
        #     for idx2, num2 in enumerate(nums):
        #         if num + num2 == target and idx != idx2:
        #             ans = [idx, idx2]

        ### Optimized Solution: use a hashmap
        hashmap = {} # key:val = num:idx
        for idx, num in enumerate(nums):
            delta = target - num
            if delta in hashmap:
                return [ hashmap[delta], idx]
            hashmap[num] = idx     