#30. 串联所有单词的子串

# 超时
# class Solution:
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         if not s or not words:
#             return []
#
#         res = set()
#         one_words = []
#         def dfs(words,one_words):
#             if len(words) == 0:
#                 str1 = "".join(one_words)
#                 temp = s.find(str1)
#                 while temp != -1:
#                     res.add(temp)
#                     temp = s.find(str1,temp+1)
#             for i in range(len(words)):
#                 dfs(words[:i]+words[i+1:],one_words+[words[i]])
#         dfs(words,one_words)
#         if -1 in res:
#             res.remove(-1)
#         return list(res)

class Solution:
    def findSubstring(self,s,words):
        if not s or not words:
            return []
        if s == ''.join(words):
            return [0]
        res = []
        index = 0
        word_len = len(words[0])
        sub_len = len(words) * word_len
        words_dict = {}
        for x in words:
            if x not in words_dict:
                words_dict[x] = 1
            else:
                words_dict[x] += 1
        while index <= len(s)-sub_len:
            sub_dict = {}
            sub_str = s[index:index + sub_len]
            while sub_str:
                if sub_str[:word_len] not in sub_dict:
                    sub_dict[sub_str[:word_len]] = 1
                else:
                    sub_dict[sub_str[:word_len]] += 1
                sub_str = sub_str[word_len:]
            flag = 1
            for x in words:
                if x not in sub_dict:
                    flag = 0
                    break
                if words_dict[x] != sub_dict[x]:
                    flag = 0
                    break
            if flag:
                res.append(index)
            index += 1
        return res

so = Solution()
s = "barfoobarfoo"
words =  ["foo","bar"]
r = so.findSubstring(s,words)
print(r)
