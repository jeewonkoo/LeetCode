class Solution:
    def getConcatenation(self, nums):
        ans = nums + [0] * len(nums)
        for i in range(len(nums)):
            ans[i+len(nums)] = nums[i] 
        return ans