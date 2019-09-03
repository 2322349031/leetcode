'''
ac
题目image/19腾讯01、01_.png
'''
class Interval_tree(object):
    def __init__(self,data):
        node = {
            'left':-1,
            'right':-1,
            'weight':0,
            'flag':0,
            'y':[]
        }
        self.tree = [node.copy() for x in range(800002)]
        self.data = data
        self.n = 0
        self.ans = 0
        self.build(1,1,len(data))
    def build(self,k,l,r):
        self.tree[k]['left'] = l
        self.tree[k]['right'] = r
        if l == r:
            self.tree[k]['weight'] = self.data[self.n]
            self.n += 1
            return
        mid = (r+l) // 2
        self.build(k*2,l,mid)
        self.build(k*2+1,mid+1,r)
        self.tree[k]['weight'] = self.tree[2*k]['weight'] + self.tree[2*k+1]['weight']
    def down(self,k):
        self.tree[2*k]['flag'] += self.tree[k]['flag']
        self.tree[2*k+1]['flag'] += self.tree[k]['flag']
        self.tree[2*k]['weight'] += self.tree[k]['flag']*(self.tree[2*k]['right'] - self.tree[2*k]['left'] + 1)
        self.tree[2*k+1]['weight'] += self.tree[k]['flag']*(self.tree[2*k+1]['right']-self.tree[2*k+1]['left']+1)
        self.tree[k]['flag'] = 0
    def ask_interval(self,k,a,b):
        if a<=self.tree[k]['left'] and self.tree[k]['right'] <= b:
            self.ans += self.tree[k]['weight']
            self.ans = self.ans
            return
        if self.tree[k]['flag']:
            self.down(k)
        mid = (self.tree[k]['left'] + self.tree[k]['right']) // 2
        if a <= mid:
            self.ask_interval(2*k,a,b)
        if b>mid:
            self.ask_interval(2*k+1,a,b)


t,k = list(map(int,input().split()))

f = [0] * 100001
if k == 1:
    f[1] = 2
else:
    f[1] = 1

for i in range(2,100001):
    if i < k:
        f[i] = 1
    elif i == k:
        f[i] = 2
    else:
        f[i] = (f[i-1] + f[i-k])% (1e9 + 7)

T = Interval_tree(f)
for g in range(t):
    a,b = list(map(int,input().split()))
    T.ask_interval(1, a+1, b+1)
    tmp = T.ans % (1e9 + 7)
    print(int(tmp))
    T.ans = (T.ans-tmp) % (1e9 + 7)
