class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t = 0
        
        for i in range(len(nums)):
            if (nums[i-t] == 0):
                del nums[i-t]
                t += 1
        for j in range(t):
            nums.append(0)
