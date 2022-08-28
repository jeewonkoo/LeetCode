class Solution:
    def longestPalindrome(self, s):
        """
        type s: str
        rtype: int
        """
        frequency = {}
        for i in s: 
            frequency[i] = frequency.get(i, 0) + 1

        longest = 0
        isOddAppear = False 
        
        for i in frequency.values(): 
            if i % 2 == 0: longest += i
            else: 
                longest += i - 1
                isOddAppear = True
                
        return longest + 1 if isOddAppear else longest

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("a"))