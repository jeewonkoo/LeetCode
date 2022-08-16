class Solution:
    def maxArea(self, height):
        """
        type height: List[int]
        return int
        """
        max_amount, curr_amount = 0, 0
        left, right = 0, len(height)-1 
        while left < right: 
            if height[left] < height[right]:
                curr_amount = height[left] * (right - left)
                left+=1
            else: 
                curr_amount = height[right] * (right - left)
                right-=1
            if max_amount < curr_amount: max_amount = curr_amount

        return max_amount 

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7])) #prints 49
    print(s.maxArea([1,1])) #prints 1
