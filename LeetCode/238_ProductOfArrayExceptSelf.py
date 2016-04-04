def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1 for i in range(len(nums))]
        length = len(nums)
        left, right = 1,1
        for i in range(length-1):
            # for result[i+1], its left is nums[0]*nums[1]*...*nums[i];
            # for result[j-1], its right is nums[length-1]*nums[length-2]*...*nums[j]
            j = length - i - 1
            left *= nums[i] # left of result[i+1]
            right *= nums[j] # right of result[j-1]
            result[i+1] *= left
            result[j-1] *= right

        return result
