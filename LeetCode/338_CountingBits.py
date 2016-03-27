class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0: return [0]
        if num == 1: return [0,1]
        result = [0,1]
        i = 1
        while i*2 < num:
            i = i * 2
            result = result + [x+1 for x in result]
        result = result + [x+1 for x in result[:i - num]]
        #return result   
        return result[:num+2]
