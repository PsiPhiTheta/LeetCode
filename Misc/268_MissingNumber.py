class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        normal = []
        
        for i in range(len(nums)+1):
            normal.append(i)
            
        return (sum(normal)-sum(nums))
