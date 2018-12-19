class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if not nums1 or not nums2: # deal with any null inputs
            return []
        
        if (len(nums1) > len(nums2)): # make sure nums2 is the largest array to save time
            nums1, nums2 = nums2, nums1
        
        out = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                out.append(nums1[i])
                nums2.remove(nums1[i])
                
        return out
