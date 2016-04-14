def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    bitmap = 0
    for num in nums:
        if bitmap & (1<<num): return num
        else: bitmap |= (1<<num)
