'''
未ac
./image/19百度01
'''

n,m = list(map(int,input().split()))

limit = list(map(int,input().split()))

a = [0,2,5,5,4,5,6,3,7,6]

dp = [[0 for i in range(len(a))] for j in range(n+1)]

for i in limit:
    dp[2][i] = int(2 / a[i])

for i in range(3,n+1):
    for j in limit:
        dp[i][j] = int(i / a[j])

_max = 0

res = []
for ind,value in enumerate(dp[n]):
    res.append([ind,value])

res.sort(key=lambda x:x[0],reverse=True)
res.sort(key=lambda x:x[1],reverse=True)


if res[0][1]*a[res[0][0]] == n:
    print(1)
    print(str(res[0][0])*res[0][1])

else:
    tmp = n - res[0][1]*a[res[0][0]]
    print(tmp)
    print(res)
    if max(dp[tmp]) == 0:
        tmp = tmp + a[res[0][0]]
        print('tmp----',tmp)
        tmp_res = []
        for ind, value in enumerate(dp[tmp]):
            tmp_res.append([ind, value])
        tmp_res.sort(key=lambda x: x[0], reverse=True)
        tmp_res.sort(key=lambda x: x[1], reverse=True)
        print(tmp_res)
        if tmp_res[0][0] > res[0][0]:
            print(2)
            print(str(tmp_res[0][0])*tmp_res[0][1]+str(res[0][0])*(res[0][1]-1))
        else:
            print(3)
            print(str(res[0][0])*(res[0][1]-1) + str(tmp_res[0][0])*tmp_res[0][1])
    else:
        tmp_res = []
        for ind, value in enumerate(dp[tmp]):
            tmp_res.append([ind, value])
        tmp_res.sort(key=lambda x: x[0], reverse=True)
        tmp_res.sort(key=lambda x: x[1], reverse=True)
        if tmp_res[0][0] > res[0][0]:
            print(4)
            print(str(tmp_res[0][0])*tmp_res[0][1]+str(res[0][0])*(res[0][1]))
        else:
            print(5)
            print(str(res[0][0])*(res[0][1]) + str(tmp_res[0][0])*tmp_res[0][1])


