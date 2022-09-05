class Solution:
    def maxProfit(self, prices):
        idx = 0
        mx_p = 0
        for i in range(1, len(prices)):
            if prices[idx] < prices[i]:
                mx_p += prices[i] - prices[idx]
            idx+=1 
        return mx_p