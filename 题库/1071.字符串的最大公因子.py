class Solution:
    def isDivides(self,sub,parent):
        ns = len(sub)
        np = len(parent)
        if np % ns != 0:
            return False
        for i in range(0,np,ns):
            if sub != parent[i:i+ns]:
                return False
        return True

    def gcdOfStrings(self, str1,str2):
        n1 = len(str1)
        n2 = len(str2)
        if n2 > n1:
            str1,str2 = str2,str1
            n1,n2 = n2,n1

        # print("str1:",str1,n1)
        # print("str2:",str2,n2)

        output = ""
        for i in range(1,n2+1):
            temp_str = str2[0:i]
            #print("temp_str:",temp_str)
            if self.isDivides(temp_str,str1) and self.isDivides(temp_str,str2):
                output = temp_str
        return output

if __name__ == '__main__':
    s = Solution()
    s1 = 'LEET'
    s2 = 'CODE'
    print(s.gcdOfStrings(s1,s2))