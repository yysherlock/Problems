class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        if len(prices)==1: return 0
        if len(prices)==2:
            return max(0,prices[1] - prices[0])
        left = 0
        right = len(prices)
        mid = (left + right) / 2

        left_max = self.maxProfit(prices[left:mid+1])
        right_max = self.maxProfit(prices[mid+1:right])
        inter_max = max(prices[mid:right]) - min(prices[left:mid+1])

        return max(left_max, right_max, inter_max)
        
