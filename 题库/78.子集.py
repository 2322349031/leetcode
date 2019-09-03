#78.子集
import copy
# class Solution:
#     def subsets(self, nums):
#         if len(nums) == 0:return [[]]
#         if len(nums) == 1:return [[],nums]
#         final = []
#         for k in self.subsets(nums[:-1]):
#             for j in self.subsets([nums[-1]]):
#                 # print("k=",k)
#                 # print("j=",j)
#                 final.append(k+j)
#                 # print("final=",final)
#         return final
class Solution:
    def subsets(self, nums):
        if len(nums) == 0:return [[]]
        if len(nums) == 1:return [[],nums]
        final = [[],[nums[0]]]
        for i in range(1,len(nums)):
            temp = [[],[nums[i]]]
            final = [a+b for a in final for b in temp]
        return final

s = Solution()
res = s.subsets([1,2,3])
print(res)



