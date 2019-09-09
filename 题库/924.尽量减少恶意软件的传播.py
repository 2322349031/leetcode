'''
ac
'''
class Solution:
    def minMalwareSpread(self, graph, initial):
        initial.sort()
        n = len(graph)
        pre = [x for x in range(n)]
        record = [[1,1,x] if x in initial else [0,1,x] for x in range(n)]
        def find(root):
            son = root
            while root != pre[root]:
                root = pre[root]
            while son != root:
                son,pre[son] = pre[son],root
            return root
        def join(x,y):
            x = find(x)
            y = find(y)
            if x != y:
                #print(x,' ',y,' ',record)
                record[x][0] += record[y][0]
                record[x][1] += record[y][1]
                record[x].extend(record[y][2:])
                record[y] = []
                pre[y] = x

        E = []
        for i in range(n):
            for j in range(i+1,n):
                if graph[i][j] == 1:
                    E.append([i,j])
        for start,end in E:
            x = find(start)
            y = find(end)
            join(x,y)
        #print(record)
        count = [r[0] for r in record if r != []]
        #print(count)
        if 1 not in count:
            return initial[0]
        res = []
        _max = 0
        for rec in record:
            if rec != []:
                if  rec[0] == 1 and rec[1] > _max:
                    _max = rec[1]
        for rec in record:
            if rec != []:
                if rec[0] == 1 and rec[1] == _max:
                    res.extend(rec[2:])
        #print(res)
        for x in initial:
            if x in res:
                return x

s = Solution()
graph = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,1,0],[0,0,0,1,1,0],[0,0,0,0,0,1]]
initial = [5,0]
print(s.minMalwareSpread(graph,initial))


