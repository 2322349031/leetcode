#23. 合并K个排序链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists==[]:
            return None
        length = len(lists)
        eliminate = []
        for i in range(len(lists)):
            if not lists[i]:
                eliminate.append(i)
        if len(eliminate) == len(lists):
            return None
        elements = []
        for head in lists:
            p = head
            while p:
                elements.append(p.val)
                p = p.next
        elements.sort()
        head = ListNode(elements[0])
        p = head
        for i in range(1,len(elements)):
            p.next = ListNode(elements[i])
            p = p.next
        return head

    def generate(self,lists):
        res = []
        for ls in lists:
            head = ListNode(ls[0])
            p = head
            for i in range(1,len(ls)):
                p.next = ListNode(ls[i])
                p  = p.next
            res.append(head)
        return res

    def show(self,head):
        p = head
        while p:
            print(p.val,'->',end='')
            p = p.next
        print('None')
    def display(self,lists):
        for head in lists:
            self.show(head)


input = [
    [1,4,5],[1,3,4],[2,6]
]
s = Solution()
input = s.generate(input)
s.display(input)
res = s.mergeKLists(input)
s.show(res)




# class Solution:
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         if lists==[]:
#             return None
#         length = len(lists)
#         eliminate = []
#         for i in range(len(lists)):
#             if not lists[i]:
#                 eliminate.append(i)
#         if len(eliminate) == len(lists):
#             return None
#         p = [x for x in lists]
#         min = 2**32
#         newNode = ListNode(min)
#         r = newNode
#         k = 0
#         for i in range(0,len(lists)):
#             if i not in eliminate:
#                 if p[i].val < newNode.val:
#                     newNode.val = p[i].val
#                     k = i
#         p[k] = p[k].next
#         if not p[k]:
#             eliminate.append(k)
#         while len(eliminate) != len(lists):
#             r.next = ListNode(2**32)
#             r = r.next
#             for i in range(0,len(lists)):
#                 #k = 0
#                 if i not in eliminate:
#                     if p[i].val < r.val:
#                         r.val = p[i].val
#                         k = i
#             p[k] = p[k].next
#             if not p[k]:
#                 eliminate.append(k)
#         return newNode
#
#     def generate(self,lists):
#         res = []
#         for ls in lists:
#             head = ListNode(ls[0])
#             p = head
#             for i in range(1,len(ls)):
#                 p.next = ListNode(ls[i])
#                 p  = p.next
#             res.append(head)
#         return res
#
#     def show(self,head):
#         p = head
#         while p:
#             print(p.val,'->',end='')
#             p = p.next
#         print('None')
#     def display(self,lists):
#         for head in lists:
#             self.show(head)
#
# input = [
#     [1,4,5],[1,3,4],[2,6]
# ]
# s = Solution()
# input = s.generate(input)
# s.display(input)
# res = s.mergeKLists(input)
# s.show(res)

