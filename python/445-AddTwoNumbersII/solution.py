# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str1 = 0
        str2 = 0

        while 1:
            if l1 is None:
                break
            str1 = str1*10+l1.val
            l1= l1.next

        while 1:
            if l2 is None:
                break
            str2 = str2*10+l2.val
            l2 = l2.next

        str1 = str(str1+str2)

        result = ListNode(None)
        a = result

        for i, ch in enumerate(str1):
            a.val = int(ch)
            a.next = ListNode(None)
            if i == len(str1)-1:
                a.next=None
            a = a.next

        return result

