class Solution:
    def isSubsequence(self, s, t):
        """
        type s: str, t: str
        rtype: bool
        """
        pointer = 0
        for i in t: 
            if pointer < len(s): 
                if s[pointer] == i: pointer += 1 
        return len(s) == pointer

if __name__ == "__main__" : 
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))