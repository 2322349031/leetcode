#13	罗马数字转整数

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        t = ['a','b','c']
        d = len(t)
        for i in range(0,len(s)):
            if i+1 < len(s):
                if s[i] == 'I' and (s[i+1]=='V' or s[i+1] == 'X'):
                    num -= 1
                    continue
                if s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                    num -= 10
                    continue
                if s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                    num -= 100
                    continue
                num += roman[s[i]]
            else:
                num += roman[s[i]]
        return num


s = [1,2,3,4]
print(len(s))