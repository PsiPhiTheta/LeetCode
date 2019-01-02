class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        zeros = 0
        ones = 0 
        twos = 0
        
        for i in range(len(nums)):
            if (nums[i] == 0):
                zeros += 1
        
        for i in range(len(nums)):
            if (nums[i] == 1):
                ones += 1
                
        for i in range(len(nums)):
            if (nums[i] == 2):
                twos += 1
        
        for i in range(zeros):
            nums[i] = 0
            
        for j in range(ones):
            nums[zeros+j] = 1
        
        for k in range(twos):
            nums[zeros+ones+k] = 2
