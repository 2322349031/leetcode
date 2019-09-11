'''
未ac
'''

n,m = list(map(int,input().split()))

money_count = []

for i in range(n):
    a,b = list(map(int,input().split()))
    money_count.append([a,b])

money_count.sort(key=lambda x:x[0],reverse=True)
print(money_count)

cnt = 0

p = 0
q = len(money_count) - 1
while p <= q:
    pass