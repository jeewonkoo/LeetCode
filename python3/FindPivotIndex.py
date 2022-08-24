class Solution:
    def pivotIndex(self, nums) -> int:
        """
        type nums: List[int]
        rtype int"""
        left_sum, right_sum, pivot = 0, 0, 0
        
        while pivot < len(nums):
            left_sum, right_sum = sum(nums[:pivot]), sum(nums[pivot+1:])
            if left_sum == right_sum: return pivot
            pivot +=1 

        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.pivotIndex([1,7,3,6,5,6])) #prints 3
    print(s.pivotIndex([1,2,3])) #prints -1
    print(s.pivotIndex([2,1,-1])) #prints 0