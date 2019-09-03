'''
80%
题目image/19顺丰01.png
并查集三元素，上司数组，find找root老大，join合并两个团伙
'''

n,m,k = list(map(int,input().split()))

pre = [x for x in range(n+1)]

def find(root):
    son = root
    while root != pre[root]:
        root = pre[root]
    while son != root:
        tmp = pre[son]
        pre[son] = root
        son = pre[son]
    return root

def join(root1,root2):
    x = find(root1)
    y = find(root2)
    if x != y:
        pre[x] = y


E = []

f = dict()
for i in range(k):
    a,b = list(map(int,input().split()))
    if f.get(b):
        E.append([f[b],a])
    else:
        f[b] = a

total = n
for start,end in E:
    x = find(start)
    y = find(end)
    if x != y:
        pre[x] = y
        total -= 1

print(total - 1)

