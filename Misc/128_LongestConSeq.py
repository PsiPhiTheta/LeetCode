class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)==0): # deal with silly inputs
            return 0
            
        nums = list(set(nums)) # remove duplicates
        nums.sort()
        
        count = 1
        max_count = 1
        
        print(nums) # for debugging 
        
        for i in range(0, len(nums)-1):
            if (nums[i]+1 == nums[i+1]):
                count += 1
            else:
                count = 1
            
            if (count > max_count):
                max_count = count
            
            memory = nums[i]
            
        return max_count
