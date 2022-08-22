from curses.ascii import SO


class Solution:
    def generateParenthesis(self, n):
        """
        type: n int
        rtype: List[str]
        """
        dp = [[] for _ in range(n+1)]
        dp[0] = []
        dp[1] = ["()"]

        for i in range(2, n+1):
            dp[i] = ["(" + k + ")" for k in dp[i-1]]
            for j in range(1, i):
                dp[i] += [x + y for x in dp[j] for y in dp[i-j]]
            dp[i] = list(set(dp[i]))
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3)) #prints(["((()))","(()())","(())()","()(())","()()()"])
    print(s.generateParenthesis(2)) #prints(["()()", "(())"])
    print(s.generateParenthesis(1)) #prints(["()"])