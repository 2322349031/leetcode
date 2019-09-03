#71. 简化路径
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        data = [x for x in path.split(sep='/') if x!='' and x!='.']
        res = []
        for x in data:
            if x == '..':
                if res:
                    res.pop()
            else:
                res.append(x)
        return '/'+'/'.join(res)


