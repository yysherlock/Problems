def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        profits = []
        for i in range(len(prices)-1):
            profits.append(prices[i+1]-prices[i])
        for i in range(len(profits)):
            if profits[i] > 0:
                result += profits[i]
        return result
