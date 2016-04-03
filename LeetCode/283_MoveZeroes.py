class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0: continue
            # nums[i] == 0
            j = i
            while j<len(nums)-1 and nums[j]==0: j+=1
            nums[i],nums[j] = nums[j],nums[i]
