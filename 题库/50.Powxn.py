#50. Pow(x, n)

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def mul(x,m):
            i = 1
            x1 = x
            if m == 1:
                return x
            while 1:
                i = i*2
                if i >= m:
                    break
                x1 = x1 * x1
            if i == m:
                return x1*x1
            else:
                return x1*mul(x,m-i/2)
        if n == 0:
            return 1.0
        res = mul(x,abs(n))
        if n < 0:
            return (1.0/res)
        else:
            return res
s = Solution()
print(s.myPow(2,3))

