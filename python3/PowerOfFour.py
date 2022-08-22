from curses.ascii import SP
import math
class Solution:
    #naive solution
    def isPowerOfFour_1(self, n):
        """
        type: int
        rtpye: bool 
        """
        target, exp = 0, 0
        while target < n: 
            target = 4 ** exp 
            exp +=1 
            if target == n: return True
        return False

    def isPowerOfFour_2(self, n):
        """
        type: int
        rtpye: bool 
        """
        return n > 0 and not n & (n - 1) and len(bin(n)) % 2

    def isPowerOfFour_3(self, n):
        """
        type: int
        rtpye: bool 
        """
        return n > 0 and math.log(n, 4).is_integer()

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour_1(16)) #prints True
    print(s.isPowerOfFour_2(5)) #prints False
    print(s.isPowerOfFour_3(1)) #prints True