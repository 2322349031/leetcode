#55. 跳跃游戏

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        length = len(nums)
        step = 1
        for i in reversed(range(length-1)):
            if nums[i] >= step:
                step = 1
            else:
                step += 1
        if step == 1:
            return True
        else:
            return False


s = Solution()
nums = [2,3,1,1,4]
s.canJump(nums)


