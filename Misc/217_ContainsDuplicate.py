class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        
        length = len(nums)
        
        if (length < 2):
            return False
        
        for i in range(length-1):
            if (nums[i] == nums[i+1]):
                return True
        
        return False
