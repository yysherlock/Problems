def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    tot = (1+n)*n / 2
    for x in nums:
        tot -= x
    return tot
