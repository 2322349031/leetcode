import collections

if __name__ == '__main__':
    n = int(input())
    A = list(map(int,input().split()))

    f = [0]*(n-1)
    lw = collections.Counter()
    l_count = 0
    rw = collections.Counter(A)
    r_count = n
    for i in range(n-1):
        lw[A[i]] = 1
        l_count += 1
        rw[A[i]] -= 1
        r_count -= 1
        f[i] = f[i-1] + (r_count-rw[A[i]]) - (l_count-lw[A[i]])
    print(" ".join(list(map(str,f))))











    # b = [0]*n
    # f = [0]*(n-1)
    # for i in range(1,n):
    #     if A[0] != A[i]:
    #         f[0] += 1
    #         b[i] = 1
    #
    # for k in range(1,n-1):
    #     for i in range(k+1,n):
    #         if A[k] != A[i]:
    #             f[k] += 1
    #             b[i] += 1
    #     f[k] = f[k] + f[k-1] - b[k]
    # f = list(map(str,f))
    # print(' '.join(f))

