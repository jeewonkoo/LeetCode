class Solution:
    def majorityElement(self, nums):
        """
        type nums: List[int;
        rtypeL int
        """
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) +1 
            if count.get(i, 0) > (len(nums) / 2): return i

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3,2,3]))
    print(s.majorityElement([2,2,1,1,1,2,2]))