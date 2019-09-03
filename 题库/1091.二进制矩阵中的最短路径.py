from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        def isExceed(_x, _y):
            if _x<0 or _x>=n or _y <0 or _y>=n:
                return True
            return False
        # dir = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
        dir = [ (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        sign = [[0]*n for i in range(n)]
        path = [[1]*n for i in range(n)]
        search_queue = deque()
        search_queue += [[0,0]]
        searched = []
        while search_queue:
            loca = search_queue.popleft()
            #print(loca)
            if not loca in searched:
                for dx,dy in dir:
                    next_x,next_y = loca[0]+dx,loca[1]+dy
                    if not isExceed(next_x,next_y) and grid[next_x][next_y] != 1:
                        path[next_x][next_y] = path[loca[0]][loca[1]] + 1
                        search_queue += [[next_x,next_y]]
        return path[n-1][n-1]

s = Solution()
matrix = [[0,0,0],[1,1,0],[1,1,0]]
print(s.shortestPathBinaryMatrix(matrix))

