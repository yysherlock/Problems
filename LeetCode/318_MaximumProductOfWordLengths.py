class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # O(N^2)
        result = 0

        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if len(set(words[i])&set(words[j]))==0:
                    cur = len(words[i])*len(words[j])
                    if cur > result: result = cur

        return result

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # bit operation
        result = 0
        elements = [0 for i in range(len(words))]

        for i in range(len(words)):
            # transfer words[i] into a sequence of number elements[i] (use 0/1 binary representation)
            for j in range(len(words[i])):
                elements[i] |= (1<< (ord(words[i][j])-ord('a')) )
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if elements[i]&elements[j]==0:
                    result = max(result, len(words[i])*len(words[j]))

        return result
