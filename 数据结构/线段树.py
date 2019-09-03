

class Interval_tree(object):
    def __init__(self,data):
        node = {
            'left':-1,
            'right':-1,
            'weight':0,
            'flag':0,
            'y':[]
        }
        self.tree = [node.copy() for x in range(10**9+1)]
        self.data = data
        self.n = 0
        self.ans = 0
        self.build(1,1,len(data))
    def build(self,k,l,r):
        self.tree[k]['left'] = l
        self.tree[k]['right'] = r
        if l == r:
            self.tree[k]['weight'] = 1
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
    def ask_point(self,k,x):
        if self.tree[k]['left'] == self.tree[k]['right']:
            self.ans = self.tree[k]['weight']
            return
        if self.tree[k]['flag']:
            self.down(k)
        mid = (self.tree[k]['left'] + self.tree[k]['right']) // 2
        if x <= mid:
            self.ask_point(2*k,x)
        else:
            self.ask_point(2*k+1,x)
    def change_point(self,k,x,y):
        if self.tree[k]['left'] == self.tree[k]['right']:
            self.tree[k]['weight'] += y
            return
        if self.tree[k]['flag']:
            self.down(k)
        mid = (self.tree[k]['left'] + self.tree[k]['right']) // 2
        if x <= mid:
            self.change_point(2*k,x,y)
        else:
            self.change_point(2*k+1,x,y)
        self.tree[k]['weight'] = self.tree[2*k]['weight'] + self.tree[2*k+1]['weight']
    def ask_interval(self,k,a,b):
        if a<=self.tree[k]['left'] and self.tree[k]['right'] <= b:
            self.ans += self.tree[k]['weight']
            return
        if self.tree[k]['flag']:
            self.down(k)
        mid = (self.tree[k]['left'] + self.tree[k]['right']) // 2
        if a <= mid:
            self.ask_interval(2*k,a,b)
        if b>mid:
            self.ask_interval(2*k+1,a,b)
    def change_interval(self,k,a,b,y):
        if a<=self.tree[k]['left'] and self.tree[k]['right'] <= b:
            self.tree[k]['weight'] += y*(self.tree[k]['right']-self.tree[k]['left']+1)
            self.tree[k]['flag'] += y
            return
        if self.tree[k]['flag']:
            self.down(k)
        mid = (self.tree[k]['left'] + self.tree[k]['right']) // 2
        if a <= mid:
            self.change_interval(2*k,a,b,y)
        if b > mid:
            self.change_interval(2*k+1,a,b,y)
        self.tree[k]['weight'] = self.tree[2*k]['weight'] + self.tree[2*k+1]['weight']

if __name__ == '__main__':
    data = [6,5,3,1,2,4,8,4]
    T = Interval_tree(data)
    for i in range(4*len(data)-1):
        if T.tree[i]['left'] != -1:
            print(T.tree[i])
    T.ask_point(1,4)
    print(T.ans)
    T.ans = 0
    T.change_point(1,4,4)
    print(T.tree[11]['weight'])
    T.ask_interval(1,1,4)
    print(T.ans)
    T.change_interval(1, 1, 4,2)
    T.ans = 0
    T.ask_interval(1,1, 4)
    print(T.ans)






