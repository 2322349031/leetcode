#14	最长公共前缀

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        t= len(strs)
        if t == 0:
            return result
        flag = True
        length = min([len(x) for x in strs])
        for i in range(0,length):
            ch = strs[0][i]
            for word in strs[1:]:
                if ch != word[i]:
                    flag = False
            if flag:
                result += ch
            else:
                break
        return result

s = Solution()
strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))