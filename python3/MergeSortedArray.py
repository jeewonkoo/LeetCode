class Solution:
    def merge_1(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        type: nums1 List[int]
              m int
              nums2 List[int]
              n int
        rtype: None
        """
        pointer_1, pointer_2, pos = m-1, n-1, len(nums1) - 1
        
        while pointer_2 >= 0: 
            if pointer_1 >= 0 and nums1[pointer_1] >= nums2[pointer_2]:
                nums1[pos] = nums1[pointer_1]
                pointer_1 -=1
            else: 
                nums1[pos] = nums2[pointer_2]
                pointer_2 -=1
            pos -=1 
        return nums1

    def merge_2(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        type: nums1 List[int]
              m int
              nums2 List[int]
              n int
        rtype: None
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1

if __name__ == '__main__':
    s = Solution()
    print(s.merge_1([1,2,3,0,0,0], 3, [2,5,6], 3)) #prints [1,2,2,3,5,6]
    print(s.merge_1([1], 1, [], 0)) #prints [1]
    print(s.merge_2([0], 0, [1], 1)) #prints [1]
    print(s.merge_2([2,0], 1, [1], 1)) #prints [1,2]

