class Solution:
    def fib_dp(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1 
        dp = [0] * (n+1)
        dp[0] = 0 
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    def fib_dp_dict(self, n: int) -> int:
        # if n <= 1: return n
        # else: return fib(n-1) + fib(n-2)
        d = {0:0, 1:1}
        for i in range(2, n+1):
            # first, second = d[i-1], d[i-2]
            d[i] = d[i-1] + d[i-2]
        return d[n]
    
    def fib_recursion(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        return self.fib(n-2) + self.fib(n-1)