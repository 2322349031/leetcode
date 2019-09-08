'''
no ac  exceed time
'''
class Solution:
    def maximumSum(self, arr):
        n = len(arr)
        f = [0] * n

        r = max(arr)
        if r <= 0:
            return r
        _max = sum(arr)
        symbol = -1
        if arr[0] < 0:
            f[0] = 0
            symbol = 0
        else:
            f[0] = arr[0]
        for i in range(1,n):
            t1 = arr[i]
            t2 = arr[i] + f[i-1]

s = Solution()

arr = [-1,-1,-1,-1]
print(s.maximumSum(arr))

