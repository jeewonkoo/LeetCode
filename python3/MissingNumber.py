from curses.ascii import SO


class Solution:
    def missingNumber_1(self, nums):
        """
        type nums: : List[int]
        rtype: int
        """
        count = [-1] * (len(nums) + 1)
        for v in nums: 
            count[v] = v
        # print(count)
        return count.index(-1)
    
    def missingNumber_2(self, nums):
        """
        type nums: : List[int]
        rtype: int
        """
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)
    
if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber_1([3,0,1])) #prints 2
    print(s.missingNumber_2([0,1])) #prints 2
    print(s.missingNumber_2([9,6,4,2,3,5,7,0,1])) #prints 8