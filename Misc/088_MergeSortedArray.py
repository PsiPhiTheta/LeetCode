class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        # we essentially need to reproduce merge sort
        
        while (m > 0 and n > 0): # m and n point to the current number being compared
            if (nums1[m-1] >= nums2[n-1]): # from end to start, if nums1 bigger than nums2
                nums1[m+n-1] = nums1[m-1] # insert nums1
                m -= 1 # move pointer of nums1
            else: # else if nums2 bigger than nums1
                nums1[m+n-1] = nums2[n-1] # insert nums2
                n -= 1 # move pointer of nums2
                
        if (n > 0): # if numbers remaining in nums2
            nums1[:n] = nums2[:n]
          
