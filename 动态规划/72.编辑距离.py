

class Solution:
    def minDistance(self, word1, word2):
        N,M = len(word1),len(word2)

        if N == 0:
            return M
        if M == 0:
            return N
        a,b = word1,word2
        f = [[0]*M for x in range(N)]

        for j in range(0,M):
            if a[0] not in b[:j+1]:
                f[0][j] = len(b[:j+1])
            else:
                f[0][j] = len(b[:j+1]) - 1

        for i in range(0,N):
            if b[0] not in a[:i+1]:
                f[i][0] = len(a[:i+1])
            else:
                f[i][0] = len(a[:i+1]) - 1

        for i in range(1,N):
            for j in range(1,M):
                if a[i] == b[j]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min([f[i-1][j-1],f[i][j-1],f[i-1][j]]) + 1
        return f[N-1][M-1]

s = Solution()
print(s.minDistance("horse","ros"))
