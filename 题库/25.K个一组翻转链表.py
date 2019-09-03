#25. k个一组翻转链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self,head,tail,pre=None):
        cur = head
        while cur != tail:
            cur.next,pre,cur = pre,cur,cur.next
        return pre

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head
        tail = head
        new_head = head
        conn = head
        num = 0
        while tail:
            num += 1
            if num == k:
                remain = tail.next
                new_head = self.reverse(head,tail=tail.next)
                conn.next = self.reverseKGroup(remain,k)
                #self.show(conn)
                break
            tail = tail.next
        return new_head
    def show(self,head):
        p = head
        while p:
            print(p.val)
            p = p.next
    def get(self):
        head = ListNode(1)
        p = head
        n = 2
        while n<=5:
            p.next = ListNode(n)
            p = p.next
            n += 1
        return head

s = Solution()
head = s.get()
s.show(head)
t = s.reverseKGroup(head,3)
s.show(t)

