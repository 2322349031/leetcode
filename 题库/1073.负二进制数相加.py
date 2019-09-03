class Solution:
    def addNegabinary(self, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        if n2 > n1:
            arr1,arr2 = arr2,arr1
            n1,n2 = n2,n1

        arr2 = [0]*(n1-n2) + arr2
        # print(arr1)
        # print(arr2)
        c = 0

        res = [0]*n1

        head = []
        for i in range(n1-1,-1,-1):
            #print("i == ",i)
            if i != 0:
                #print(c)
                res[i] = arr1[i] + arr2[i] + c
                c = 0
                if res[i] == 2:
                    res[i] = 0
                    c = -1
                elif res[i] == -1:
                    res[i] = 1
                    c = 1
                elif res[i] == 3:
                    res[i] = 1
                    c = -1
            else:
                res[i] = arr1[i] + arr2[i] + c
                c = 0
                if res[i] == 2:
                    res[i] = 0
                    head = [1,1]
                elif res[i] == -1:
                    res[i] = 1
                    head = [1]
                elif res[i] == 3:
                    res[i] = 1
                    head = [1,1]

            #print(res)

        res = head + res
        index = -1
        if sum(res) == 0:
            res = [0]
            return res

        for i in range(0,len(res)):
            if res[i] == 1:
                break
            else:
                index = i

        res = res[index+1:]
        return res



if __name__ == '__main__':
    s = Solution()
    arr1 = [1, 1, 1, 1, 1]
    arr2 = [1, 0, 1]
    print(s.addNegabinary(arr1,arr2))