class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        length = len(nums)
        
        temp = 1
        for i in range(0,length):
            result.append(temp)
            temp = temp * nums[i]
        
        temp = 1
        for i in range(length-1,-1,-1):
            result[i] = result[i] * temp
            temp = temp * nums[i]
            
        return result #O(1) space, O(n) time
