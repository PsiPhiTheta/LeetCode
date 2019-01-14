class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        
        if not nums:
            return ans
        
        for i in nums:
            for idx in range(len(ans)):
                ans.append(ans[idx]+[i])
        
        return ans
        
