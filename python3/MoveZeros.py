class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        type nums: List[int]
        """
        zero = 0
        for non_zero in range(len(nums)):
            if nums[non_zero] != 0 and nums[zero] == 0: 
                nums[non_zero], nums[zero] = nums[zero], nums[non_zero]
            if nums[zero] != 0: zero += 1