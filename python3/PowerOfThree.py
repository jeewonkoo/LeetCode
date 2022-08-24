class Solution:
    def isPowerOfThree_1(self, n):
        """
        type n: int
        rtype bool
        """
        target, counter = 0, 0
        while target < n:
            target = 3 ** counter
            counter +=1
            if target == n: return True
        return False

    def isPowerOfThree_2(self, n):
        """
        type n: int
        rtype bool
        """
        while n > 0:
            if n == 1: return True
            n /= 3
        return False 

if __name__ == '__main__': 
    s = Solution()
    print(s.isPowerOfThree_1(1)) #prints True
    print(s.isPowerOfThree_1(-1)) #prints False
    print(s.isPowerOfThree_2(3))  #prints True
    print(s.isPowerOfThree_2(0))  #prints False