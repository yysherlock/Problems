class Solution(object):
    result = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.process([],nums)
        return self.result

    def process(self, re, nums):
        if len(nums)==0:
            self.result.append(re)
            return
        for i in range(len(nums)):
            cur = nums[i]
            nums.pop(i)
            self.process(re+[cur], nums)
            nums.insert(i,cur)

        
