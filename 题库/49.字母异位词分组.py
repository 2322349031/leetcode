#49. 字母异位词分组

class Solution:
    def getKeys(self,word):
        num = 0
        for i in range(len(word)):
            temp = ord(word[i]) - 97
            num += temp*temp
        return num
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        rem = {}
        for index,word in enumerate(strs):
            #key = self.getKeys(word)
            key = "".join(sorted(word))
            if key not in rem:
                rem[key] = [word]
            else:
                rem[key].append(word)
        if not rem:
            return []
        res = []
        for key,value in rem.items():
            res.append(value)
        return res

s = Solution()
args = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(args))

