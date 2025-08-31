class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = list(range(len(cost) + 1))

        memo[0] = 0
        memo[1] = 0

        for i in range(2, len(cost) + 1):
            memo[i] = min(memo[i-1] + cost[i-1], memo[i-2] + cost[i-2])

        return memo[len(cost)]

        # cost = 10,15,20
        # memo = 0,0,10,15
        
