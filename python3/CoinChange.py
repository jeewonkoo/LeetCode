#Use Dynamic programming 
class Solution:
    def coinChange(self, coins, amount):
        """
        type coins: List[int]
             amount: int
        return int
        """
        if amount == 0: return 0 
        dp = [float('inf') for _ in range(amount+1)]
        #if amount == 0, there is no combination
        dp[0] = 0
        for i in range(amount+1): #iterate amount to add combination up
            for coin in coins: 
                #if coin is greater than amount, there is no combination
                if i - coin >= 0: 
                    #since we need fewest number of coins, use min()
                    #there is dp[i] combination for amount i
                    dp[i] = min(dp[i], dp[i-coin]+1)
                    
        #return combination if exists, otherwise returns -1            
        return dp[-1] if dp[-1] != float('inf') else -1

if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1,2,5], 11)) #prints 3
    print(s.coinChange([2], 3)) #prints -1
    print(s.coinChange([1], 0)) #prints 0