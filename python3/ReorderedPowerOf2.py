import itertools

class Solution:
    def reorderedPowerOf2(self, n):
        """
        type n: int
        rtype: bool
        """
        for cand in itertools.permutations(str(n)):
            if cand[0]!='0' and bin(int("".join(cand))).count('1') ==1:
                return True
        return False

if __name__ == "__main__": 
    s = Solution()
    print(s.reorderedPowerOf2(1))
    print(s.reorderedPowerOf2(10))