#73.73.	矩阵置零

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        row_len = len(matrix)
        col_len = len(matrix[0])
        row_list = [0 if 0 in x else 1 for x in matrix]
        col_list = [1 for i in range(col_len)]
        for i in range(row_len):
            temp = matrix[i]
            start = 0
            end = col_len
            while 0 in temp[start:end]:
                c = temp.index(0,start,end)
                col_list[c] = 0
                start = c + 1
        print(row_list)
        print(col_list)
        for i in range(row_len):
            for j in range(col_len):
                if row_list[i] == 0:
                    matrix[i][j] = 0
                    continue
                if col_list[j] == 0:
                    matrix[i][j] = 0
        return matrix

s = Solution()
t = [[0,0,0,5],
     [4,3,1,4],
     [0,1,1,4],
     [1,2,1,3],
     [0,0,1,1]]
print(s.setZeroes(t))