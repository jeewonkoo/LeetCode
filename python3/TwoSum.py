class Solution:
    def twoSum(self, nums, target):
        """
        type nums: List[int]
             target: int
        return List[int]
        """
        for i, v in enumerate(nums):
            if target-v in nums and nums.index(target-v) != i: 
                return [i, nums.index(target-v)]
            