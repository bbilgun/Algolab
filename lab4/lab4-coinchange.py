class Solution:
#dnmk zoosnii jagsaalt, gargah mungunii hemjee. Hamgin tsuun zoosni too bolomjgu bol -1 iig butsaana
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) #0-amount hurtel buh ded asuudlig hadgalna
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins: #zoosni utgiin jagsaaltaar davtald yvuulna
                if i - coin >= 0: #mungun dunges zoosni dung hasch boljiwl urgeljilne
                    dp[i] = min(dp[i], dp[i - coin] + 1) 

        return dp[amount] if dp[amount] != float('inf') else -1
