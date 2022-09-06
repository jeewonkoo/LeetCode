class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return
        k %= len(nums)
        
        def reverse(nums, l, r):
            while l <= r: 
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        l, r = 0, len(nums)-1
        reverse(nums, l, r)
        reverse(nums, l, k-1)
        reverse(nums, k, r)
        
        # # print(k)
        # temp = nums[k]
        # for i in range(len(nums)//2):
        #     # print(nums[k+i])
        #     nums[i], nums[k+i] = nums[-k+i], nums[i]
        #     # print(nums[-k+i])
        #     print(nums)
        # if len(nums) % 2 == 1: nums[-1] = temp

