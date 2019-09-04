'''
ac
题目image/19携程01.png
'''

def merge(intervals):
    # 0. Deal with edge cases
    if len(intervals) == 0:
        return []
    # 1. Sort the input by start-time, tie-breaking by end-time
    intervals_sorted = sorted(intervals, key=lambda x:x[0])
    # 2. Heart of the algorithm
    insert_interval = intervals_sorted[0]
    res = []
    for curr_interval in intervals_sorted[1:]:
        # if the intervals overlap --> potentially expand the interval to be inserted
        if curr_interval[0] <= insert_interval[1]:
            insert_interval[1] = max(insert_interval[1], curr_interval[1])
        # otherwise, add the interval to be inserted into the result set, and start-up a new one
        else:
            res.append(insert_interval)
            insert_interval = curr_interval
    # 3. Deal with the fence-post straggler
    res.append(insert_interval)
    return res

s = input()

dic = dict()

for i in range(len(s)):
    if dic.get(s[i]):
        dic[s[i]].append(i)
    else:
        dic[s[i]] = [i]

interval = []

for key,value in dic.items():
    interval.append([min(value),max(value)])

#print(interval)
interval = merge(interval)

res = [str(x[1]-x[0]+1) for x in interval]
print(','.join(res))
