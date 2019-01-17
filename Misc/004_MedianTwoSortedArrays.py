class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Target complexity is O(log(n+m))
        
        nums1.extend(nums2)
        nums1.sort() # since this uses Tim sort (a hybrid of mergesort & insertion), O(1)
        
        if (len(nums1)<2):
            return nums1[0]
        elif (len(nums1)%2):
            return nums1[len(nums1)//2]
        else:
            left  = nums1[(len(nums1)-1)//2]
            right = nums1[(len(nums1)+1)//2]
            return (left + right) / 2.0
