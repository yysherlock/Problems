def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        result = True
        for c in s:
            dic.setdefault(c,0)
            dic[c] += 1
        for c in t:
            dic.setdefault(c,0)
            dic[c] -= 1
        for k,v in dic.items():
            result = result and (not v)
            
        return result
