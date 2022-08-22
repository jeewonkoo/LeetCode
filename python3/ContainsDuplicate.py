class Solution:
    def containsDuplicate_1(self, nums):
        """
        type nums:  List[int]
        rtype: bool
        """
        return len(set(nums)) != len(nums)
    
    def containsDuplicate_2(self, nums):
        """
        type nums:  List[int]
        rtype: bool
        """
        seen = {}
        for i in nums: 
            if i in seen: return True
            seen[i] = seen.get(i, 0) + 1
        return False

if __name__ == '__main__': 
    s = Solution()
    print(s.containsDuplicate_1([1,2,3,1])) #prints True
    print(s.containsDuplicate_2([1,2,3,4])) #prints False
    print(s.containsDuplicate_2([1,1,1,3,3,4,3,2,4,2])) #prints True