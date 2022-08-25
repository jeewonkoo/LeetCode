class Solution:
    def numDecodings(self, s):
        """
        type s: str
        rtype: int 
        """
        dp = [0 for _ in range(len(s)+1)]
        
        dp[0] = 1
        dp[1] = 0 if s[0] == "0"else 1
        

        for i in range(2, len(s)+1):
            if 0 < int(s[i-1:i]) < 10: 
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26: 
                dp[i] += dp[i-2]
                
        return dp[-1]

if __name__ == '__main__' : 
    s = Solution()
    print(s.numDecodings("11106"))  #2
    print(s.numDecodings("226"))    #3
    print(s.numDecodings("06"))     #0