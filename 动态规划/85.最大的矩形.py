
class Solution:
    def maximalRectangle(self,matrix):
        if matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0]*n; right=[n]*n; height=[0]*n
        print("left:", left)
        print("right:", right)
        print("height:", height)
        maxA = 0
        for i in range(m):
            print("row {}:".format(i))
            cur_left = 0; cur_right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j],cur_left)
                else:
                    height[j] = 0
                    left[j]=0;cur_left += 1
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j],cur_right)
                else:
                    right[j] = n
                    cur_right = j
            print("left:",left)
            print("right:",right)
            print("height:",height)
            for j in range(n):
                maxA = max(maxA, (right[j] - left[j]) * height[j])
        return maxA





matrix =[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

matrix = [
    ['0','0','0','1','0','0','0'],
    ['0','0','1','1','1','0','0'],
    ['0','1','1','1','1','1','0']
]
s = Solution()
res = s.maximalRectangle(matrix)
print(res)


