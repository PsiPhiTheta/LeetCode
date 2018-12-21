class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        out = []
        for i in nums1:
            if ((i not in out) and (i in nums2)):
                out.append(i)
    
        return out
