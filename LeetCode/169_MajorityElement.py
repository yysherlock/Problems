def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for x in nums:
            dic.setdefault(x, 0)
            dic[x] += 1
            if dic[x] > round((len(nums)-1)/2.0): return x
