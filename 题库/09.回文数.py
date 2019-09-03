class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list1 = [i for i in str(x)]
        k = 0
        b = 0
        for k in range(0,len(list1)):
            b = len(list1) - k - 1
            if list1[k] != list1[b] or k>=b:
                break

        if k>=b:
            return True
        else:
            return False