#整数反转

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        symbol = ''
        if x[0] == '-':
            x = x[1:]
            symbol = '-'
        list1 = [i for i in str(x)]
        list1.reverse()
        value = int(symbol + ''.join(list1))
        if value < -2**31 or value > 2**31-1:
            return 0
        return value

s = Solution()
s.reverse(-123)