from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i in range(1, len(prices)): #ehnii udrus suulin udur hurtel shalgana. umnuh udurtei haritsuulj ashig oloh gj uzne
            if prices[i] > prices[i - 1]:#unuudrin une uchigrihus ih baiwl maxru nemne 
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit

prices = [7, 1, 5, 3, 6, 4]

solution = Solution()

result = solution.maxProfit(prices)
print(result)
