from curses.ascii import SO


class Solution:
    def runningSum(self, nums):
        """
        type nums: List[int]
        rtype List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
    
if __name__ == '__main__' : 
    s = Solution()
    print(s.runningSum([1,2,3,4]))  #prints [1,3,6,10]
    print(s.runningSum([1,1,1,1,1]))    #prints [1,2,3,4,5]
    print(s.runningSum([3,1,2,10,1]))  #prints [3,4,6,16,17]
