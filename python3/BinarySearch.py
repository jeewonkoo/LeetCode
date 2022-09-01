class Solution:
    def search(self, nums, target):
        """
        type nums:  List[int], target: int
        rtpye: int
        """
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid +1
            else: return mid
        return -1
                
if __name__ == "__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))
    print(s.search([-1,0,3,5,9,12], 2))