def hammingWeight(n):
   """
   :type n: int
   :rtype: int
   """
   count = 0
   for i in range(32):
       if (1<<i) & n: count += 1
   return count

print hammingWeight(2)
print hammingWeight(3)
print hammingWeight(11)
