class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profix = 0
        sortp= sorted(prices, reverse = True)
        if prices == sortp:
            return 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j]>prices[i]:
                    max_profix = max(max_profix, prices[j]-prices[i])
                else:
                    break
        return max_profix