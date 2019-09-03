#21. 合并两个有序链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            p = l1
            l1 = l1.next
        else:
            p = l2
            l2 = l2.next
        r = p
        if not l1:
            p.next = l2
            return p
        if not l2:
            p.next = l1
            return p
        while l1 or l2:
            if l1.val <= l2.val:
                r.next = l1
                l1 = l1.next
                r = r.next
                if not l1:
                    r.next = l2
                    break
            else:
                r.next = l2
                l2 = l2.next
                r = r.next
                if not l2:
                    r.next = l1
                    break
        return p
# class Solution:
#
#
