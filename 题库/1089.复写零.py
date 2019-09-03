class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        move = [0] * len(arr)
        count = 0
        for i in range(len(arr)):
            move[i] = count
            if arr[i] == 0:
                count += 1
        #print(move)
        for i in range(len(arr)-1,-1,-1):
            new_index = i + move[i]
            if new_index >= len(arr):
                continue
            arr[new_index] = arr[i]
            if arr[new_index] == 0 and new_index+1<len(arr):
                arr[new_index+1] = 0
        #print(arr)




#t = [1,0,2,3,0,4,5,0]
t = [1,2,3]
s = Solution()
s.duplicateZeros(t)
