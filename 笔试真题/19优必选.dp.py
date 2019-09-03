'''
ac
题目image/19优必选01.png
'''

class Solution:
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]  # 初始化dp
        dp[r][c] = 1
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]  # 初始化当前dp
            for r in range(N):
                for c in range(N):
                    for dr, dc in zip((2,-2,0,0), (0,0,2,-2)):  # 四个方向
                        if 0 <= r + dr < N and 0 <= c + dc < N:  # 判断是否出界
                            dp2[r+dr][c+dc] += dp[r][c] / 4.0  # 保留棋盘内的概率（除以4，是因为有4个方向，每个方向是4分之一）
            dp = dp2  # 更新steps-1步骤中的棋盘概率数据
        return sum(map(sum, dp))  # 把落在棋盘上的所有位置的概率加起来，就是最后落在棋盘上的概率


if __name__ == '__main__':
    solu = Solution()
    input_list = list(map(int,input().split(',')))
    N = input_list[0]
    K = input_list[1]
    i = input_list[2]
    j = input_list[3]
    print(solu.knightProbability(N,K,i,j))