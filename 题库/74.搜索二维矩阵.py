#74. 搜索二维矩阵
class Solution:
    # 二分法
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        if row==0 or col == 0:
            return False
        left = 0
        right = row*col-1
        while left<=right:
            mid = int((left + right)/2)
            temp = matrix[int(mid/col)][mid%col]
            if temp == target:
                return True
            elif temp > target:
                right = mid-1
            else:
                left = mid+1
        return False
