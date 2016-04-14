def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    bitmap = 0
    for i in range(32):
        count = 0
        for num in nums:
            count += ((1 << i) & num) >> i
        resBit = count % 3 # 0 or 1, according to the problem, every number appears 3 times or once.

        if i==31 and resBit: # represents negative number
            bitmap -= 1<<31
        else: bitmap |= (resBit << i)

    return bitmap
