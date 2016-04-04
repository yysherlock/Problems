def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        elems = set({})
        for elem in nums:
            if elem in elems:
                return True
            else: elems.add(elem)
        return False
