# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import math

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum_list = []
                
        l1_sum = 0
        i = 0
        while l1.next is not None:
            l1_sum += l1.val*(10**i)
            i += 1
            l1 = l1.next
        l1_sum += l1.val*(10**i)
        
        l2_sum = 0
        i = 0
        while l2.next is not None:
            l2_sum += l2.val*(10**i)
            i += 1
            l2 = l2.next
        l2_sum += l2.val*(10**i)
                
        l1_plus_l2 = l1_sum + l2_sum
        
        if (l1_plus_l2 == 0):
            return [0]
        
        while (l1_plus_l2 != 0):
            temp = l1_plus_l2 % 10
            sum_list.append(temp)
            l1_plus_l2 = l1_plus_l2 // 10
            
        return sum_list
