from curses.ascii import SO


class Solution:
    def maxProfit_1(self, prices):
        """
        type:  List[int]
        rtype: int
        """
        left, right, max_profit = 0, 1, 0
        while right < len(prices):
            curr_profit = (prices[right] - prices[left])
            if curr_profit < 0:
                left = right
            if curr_profit > max_profit: max_profit = curr_profit 
            right+=1 
        
        return max_profit
    
    def maxProfit_2(self, prices):
        """
        type:  List[int]
        rtype: int
        """
        max_profit, minimum = 0, float('inf')
        for v in prices:
            if (v < minimum): minimum = v
            elif (v > minimum): max_profit = max(v - minimum, max_profit)
        return max_profit

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit_1([7,1,5,3,6,4])) #prints 5
    print(s.maxProfit_2([7,6,5,4,3])) #prints 0