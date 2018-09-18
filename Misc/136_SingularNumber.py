from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        min_count = n + 1
        curr_count = 1
        ans = 0
        for i in range(1, n):
            if (nums[i] == nums[i - 1]):
                curr_count = curr_count + 1
            else:
                if (curr_count < min_count):
                    min_count = curr_count
                    ans = nums[i - 1]
                curr_count = 1

        if (curr_count < min_count):
            min_count = curr_count
            ans = nums[n - 1]
     
        return ans
