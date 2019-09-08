'''
ac
'''
class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        all = sum(distance)

        if start <= destination:
            pre = sum(distance[start:destination])
        else:
            pre = sum(distance[destination:start])

        if pre > all - pre:
            return all - pre
        else:
            return pre