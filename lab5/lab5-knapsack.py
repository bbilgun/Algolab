def knapsack(W, weights, values, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0: #jingin hyzgaar 0 bol 0iig butsaana
                dp[i][w] = 0
            elif weights[i - 1] <= w:#jingin hyzgart bagtj bvl
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])#odo bga itemni uldsen jingin hmgin ih uniig nemne
            else:
                dp[i][w] = dp[i - 1][w]#bagtku bol umnuhus hmgin uneteig ashiglana

    return dp[n][W] #jin w tei tentseh uyd hmmgin ih unetei bgag butsaana

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)
print(knapsack(W, weights, values, n)) 
