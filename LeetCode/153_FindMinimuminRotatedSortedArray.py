class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left, right = 0, length-1

        while left < right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right) / 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else: right = mid

        return nums[left]
