class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol = []
        prev_vol = 0
        max_vol = 0
        
        for start in range(0, len(height)-1):
            for end in range(start+1, len(height)):
                dist = (end-start)
                cur_vol = min(height[start], height[end])*dist
                if (cur_vol > max_vol):
                    max_vol = cur_vol
                    
        return max_vol
        
        #note this is an O(n^2) solution
