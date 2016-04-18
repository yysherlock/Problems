class Solution(object):
    re = []
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.re = []
        self.construct('',n,n)
        return self.re

    def construct(self,cur,left,right):
        if left==0 and right==0:
            self.re.append(cur)
            return
        # if left==right, put a '('; if left < right, put a '(' or ')'
        if left == right: # put a '('
            self.construct(cur+'(',left-1,right)
        if left < right:
            # put a '(' or ')'
            if left > 0: # if left==0, only put a ')'
                self.construct(cur+'(',left-1,right)
            self.construct(cur+')',left,right-1)

    def naive_generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==1: return ['()']
        if n==2: return ['()()','(())']
        result = set({})
        for i in range(1,n/2+1):
            n1 = i; n2 = n-n1
            for s1 in self.generateParenthesis(n1):
                for s2 in self.generateParenthesis(n2):
                    if n1==1: result.add('('+s2+')')
                    result.add(s1+s2)
                    result.add(s2+s1)

        return list(result)
