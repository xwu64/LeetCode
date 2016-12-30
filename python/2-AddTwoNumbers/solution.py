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
        s1 = []
        s2 = []

        start = l1
        while start:
            s1.append(start.val)
            start = start.next

        start = l2
        while start:
            s2.append(start.val)
            start = start.next


        sum = 0

        for i in range(len(s1)):
            sum = sum + 10**i*s1[i]

        for i in range(len(s2)):
            sum = sum + 10**i*s2[i]

        listSum = list(str(sum))
        result = ListNode(None)
        start = result
        start.val = int(listSum[-1])
        listSum.pop()

        while listSum:
            start.next = ListNode(int(listSum.pop()))
            start = start.next

        return result
