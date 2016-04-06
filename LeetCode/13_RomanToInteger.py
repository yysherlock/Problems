class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i = 0

        while i<len(s):
            pre = 4000 if i-1<0 else dic[s[i-1]]
            cur = dic[s[i]]
            post = 0 if i+1==len(s) else dic[s[i+1]]
            if cur < post:
                result = result - cur + post
                i += 2
            else:
                result = result + cur
                i += 1
        return result
