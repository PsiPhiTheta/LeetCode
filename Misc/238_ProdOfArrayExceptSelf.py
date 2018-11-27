import numpy as np

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        length = len(nums)
        
        for i in range(length):
            temp = np.asarray(nums)
            temp = np.delete(temp, i)
            product = int(np.prod(temp))
            result.append(product)
            
        return result #note passes 16/17 test cases (brute force approach)
