#滑窗法

class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        if len(customers) == 0:
            return 0
        tup = list(zip(customers,grumpy))
        print(tup)
        sum = 0
        for i in range(0,X):
            sum += tup[i][0]
        for i in range(X,len(tup)):
            if tup[i][1] == 0:
                sum += tup[i][0]
        print(sum)
        _max = sum
        for i in range(X,len(tup)):
            left = i - X
            if tup[left][1] == 1:
                sum -= tup[left][0]
            if tup[i][1] == 1:
                sum += tup[i][0]
            print("i=",i,"---sum=",sum)
            if sum > _max:
                _max = sum
        return _max




if __name__ == '__main__':
    s = Solution()
    t1 = [1, 0, 1, 2, 1, 1, 7, 5]
    arg2 = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    s.maxSatisfied(t1,arg2,X)