class Solution:
    def minCostClimbingStairs(self, cost):
        """
        type cost: List[int]
        rtype: int
        """
        cost.extend([0])

        for i in range(2, len(cost)):
            cost[i] += min(cost[i-2], cost[i-1])
        
        return cost[-1]