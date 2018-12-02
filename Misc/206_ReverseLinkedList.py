# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rev = None
        
        while head:
            cur = head
            head = head.next
            cur.next = rev
            rev = cur
        
        return rev
