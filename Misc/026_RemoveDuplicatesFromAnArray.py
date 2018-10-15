class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) < 2):
            return len(nums)
        
        previous = 0
        for i in range(1,len(nums)):            
            if nums[i]!=nums[previous]:
                previous += 1
                nums[previous] = nums[i]
                
            
        return (previous+1)
        
