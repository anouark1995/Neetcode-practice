class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i=0
        j=1
        profits = set()
        while j < len(prices):
            if prices[j] <= prices[i]:
                i = j
                j += 1
            else:
                profit = prices[j] - prices[i]
                profits.add(profit)
                j+=1
        if not profits:
            return 0
        else:
            return max(profits)

profit = Solution()
print(profit.maxProfit([10,1,5,6,2,1]))