from curses.ascii import SP


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        type nums: : List[int]
        rtype None
        """
        start, end, pivot = -1, -1, -1
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]: 
                start = end = max(start, i) 
                pivot = start - 1
            
            if nums[i] > nums[pivot] and i >= start: 
                end = max(end, i)

        if start == -1: 
            return nums[::-1]
        
        nums[pivot], nums[end] = nums[end], nums[pivot]
        nums[start:] = nums[start:][::-1]
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([1,2,3])) #prints [1,3,2]
    print(s.nextPermutation([3,2,1])) #prints [1,2,3]
    print(s.nextPermutation([1,1,5])) #prints [1,5,1]