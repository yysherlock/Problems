class Solution(object):

    dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    bases = sorted(dic.keys(), reverse=True)

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return ''

        for i in [0,2,4,6]:
            base1 = self.bases[i]
            base5 = base1 * 5
            base10 = base1*10

            if num < base1: continue

            p1 = (num / base1) * base1
            p2 = num % base1

            if p1 == base10 - base1:
                return self.dic[base1] + self.dic[base10] + self.intToRoman(p2)

            if p1 == base5: return self.dic[base5] + self.intToRoman(p2)
            if p1 == base5 - base1:
                return self.dic[base1] + self.dic[base5] + self.intToRoman(p2)
            if p1 > base5: return self.dic[base5] + self.intToRoman(num - base5)
            if num < base5 and num % base1 == 0: return self.dic[base1] * (num/base1)

            return self.intToRoman(p1) + self.intToRoman(p2)
            
