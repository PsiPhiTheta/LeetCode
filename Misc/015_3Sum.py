class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        
        N = len(nums)
        ans = []
        
        for i in range(N):
            if (i > 0 and nums[i] == nums[i-1]): # don't waste time on duplicate i 
                continue
                
            target = -nums[i] # set target i
            start = i+1 # set start j
            end = N-1 # set end k
            
            while (start<end):
                if (nums[start]+nums[end] == target): # sum hits target
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1 
                    while (start < end and nums[start] == nums[start-1]): # loop through duplicates
                        start += 1
                
                elif (nums[start] + nums[end] < target): # sum too small
                    start += 1 #increase sum
                
                else: # sum too large
                    end -= 1 # decrease sum
        
        return ans
