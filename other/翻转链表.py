class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    #迭代实现反转链表
    # def reverseList(self,head):
    #     p = head
    #     q = head.next
    #     r = q
    #     p.next = None
    #     while q!=None:
    #         r = r.next
    #         q.next = p
    #         p = q
    #         q = r
    #     #self.display(p)
    #     return p
    #递归实现反转链表
    def reverseList(self,head):
        if head==None or head.next==None:
            return head
        p = self.reverseList(head.next)
        q = head
        q.next = None
        r = p
        while r.next != None:
            r = r.next
        r.next = q
        return p


    def display(self,head):
        p = head
        while p!=None:
            print("%d "%p.val,end="")
            p = p.next

if __name__ == '__main__':
    ls = []
    for i in range(0,5):
        ls.append(ListNode(i+1))
    for i in range(0,4):
        ls[i].next = ls[i+1]
    p = ls[0]
    s = Solution()
    q = s.reverseList(p)
    s.display(q)
    # while p != None:
    #     print('%d '%p.val,end="")
    #     p = p.next