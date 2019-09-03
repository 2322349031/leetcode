'''
0-1背包动态规划
'''

if __name__ == '__main__':
    N,M = map(int,input().split())
    W = [0]*(N+1)
    D = [0]*(N+1)
    for i in range(1,N+1):
        W[i],D[i] = map(int,input().split())
    arr = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1,M+1):
        if W[1] <= i:
            arr[1][i] = D[1]
    for i in range(2,N+1):
        for j in range(1,M+1):
            if j-W[i]>= 0:
                arr[i][j] = max(arr[i-1][j],arr[i-1][j-W[i]]+D[i])
            else:
                arr[i][j] = arr[i-1][j]
    print(arr[N][M])


