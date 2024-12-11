class Solution: #ugsuhud hmgin baga zarlig olno shatnii oroid garh hmgin baga zardliig butsaana
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)#shatnii too cost-iin urttai tentsuu 
        dp = [0] * n #end hamgin baga zardludig hadgalna
        
        dp[0] = cost[0] 15
        dp[1] = cost[1] 20

        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i] #i-1 umnuh shatnd hureh hmgin baga zardl 

        return min(dp[n - 1], dp[n - 2]) #dp n-1 suulin shatand zogsoh n-2 umnuh shatand ni zogsood algasch usreh
15 20 40 30
dp2 = min(20, 15+)40=55
dp3 = min 55 , 20+30 = 50