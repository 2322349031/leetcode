#32.最长有效括号

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        f = [0 for x in range(len(s))]
        for i in range(1,len(s)):
            if s[i] == '(':
                f[i] = 0
                continue
            else:
                if s[i-1] == '(':
                    f[i] = f[i-2] + 2
                elif i-f[i-1]-1>=0 and s[i-f[i-1]-1] == '(':
                    if i-f[i-1]-2 < 0:
                        f[i] = f[i-1] + 2
                    else:
                        f[i] = f[i-1] + f[i-f[i-1]-2] + 2
        return max(f)

s = Solution()
t = ")()())"
print(s.longestValidParentheses(t))
