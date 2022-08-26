class Solution:
    def mySqrt(self, x):
        """
        type x: int
        rtype: int
        """
        left, right = 0, x
        while left <= right: 
            mid = (left + right) // 2
            if mid * mid <= x < (mid+1)*(mid+1): return mid
            elif x < mid*mid: right = mid - 1
            else: left = mid + 1
        return mid

if __name__ == '__main__': 
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))