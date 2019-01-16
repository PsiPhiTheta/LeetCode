class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Target space O(1), time O(n)
        
        length = len(nums)
        k = 0
        
        # Step 1. Move good numbers to start
        for i in range(len(nums)):
            if (nums[i] > 0 and nums[i] <= length):
                nums[k] = nums[i] # move good numbers to start
                k += 1 # store amount of good numbers
        
        print(nums)
        
        # Step 2. Make all numbers -1 except ans-1
        for i in range(k): 
            idx = abs(nums[i]) # set next index 
            
            if (nums[idx-1] > 0): # 
                nums[idx-1] *= -1 # make number negative
        
        print(nums)
        
        # Step 3. Look for last remaining non-negative int (if any)
        for idx in range(k): 
            if nums[idx] >= 0: 
                return idx+1 # return idx+1
        return k+1 # else return worst case
    
    # Some illustrative examples:
    
    # e.g. [1,2,0]
    # Step 1. nums stays as [1,2,0]
    # Step 2a. idx = 1, nums[0]=1 > 0 so nums[0]=-1
    # Step 2b. idx = 2, nums[1]=2 > 0 so nums[1]=-2
    # Step 3. returns k+1 (3)
    
    # e.g. [3,4,-1,1]
    # Step 1. nums becomes [3,4,1,1]
    # Step 2a. idx = 3, nums[2]=1 > 0 so nums[2]=-1
    # Step 2b. idx = 4, nums[3]=1 > 0 so nums[3]=-1
    # Step 2c. idx = 1, nums[0]=3 > 0 so nums[0]=-3
    # Step 2d. idx = 1, nums[0]=-3 so DO NOTHING
    # Step 3. returns i+1 (2)
    
    # e.g. [7,8,9,11,12]
    # Step 1. nums stays as [7,8,9,11,12] (all unreasonable)
    # Step 2. this step is skipped as there are no reasonable numbers
    # Step 3. returns i+1 (1)
    
    # e.g. [1,2,3,5,6]
    # Step 1. nums stays as [1,2,3,5,6]
    # Step 2a. idx = 1, nums[0]=1 so nums[0]=-1 
    # Step 2b. idx = 2, nums[1]=2 so nums[1]=-2 
    # Step 2c. idx = 3, nums[2]=3 so nums[2]=-3 
    # Step 2d. idx = 5, nums[4]=6 so nums[4]=-6 
    # Step 3. returns i+1 (4)
    
    # e.g. [2,1,5,6,3]
    # Step 1. nums becomes [2,1,5,3,3]
    # Step 2a. idx = 2, nums[1]=1 so nums[1]=-1 
    # Step 2b. idx = 1, nums[0]=2 so nums[0]=-2 
    # Step 2c. idx = 5, nums[4]=3 so nums[4]=-3 
    # Step 2d. idx = 3, nums[2]=5 so nums[2]=-5 
    # Step 3. returns i+1 (4)
    
    # e.g. [2,1,5,1,2,3,3]
    # Step 1. nums stays [2,1,5,1,2,3,3]
    # Step 2a. idx = 2, nums[1]=1 so nums[1]=-1 
    # Step 2b. idx = 1, nums[0]=2 so nums[0]=-2 
    # Step 2c. idx = 5, nums[4]=2 so nums[4]=-2 
    # Step 2d. idx = 1, nums[0]=2 so nums[0]=-2 
    # Step 2e. idx = 2, nums[1]=1 so nums[1]=-1 
    # Step 2f. idx = 3, nums[2]=5 so nums[2]=-5 
    # Step 2g. idx = 3, nums[2]=5 so nums[2]=-5 
    # Step 3. returns i+1 (4)
