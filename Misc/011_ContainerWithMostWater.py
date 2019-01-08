class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol = 0
        start = 0
        end = len(height)-1
        
        while (start < end):
            max_vol = max(max_vol, min(height[start], height[end])*(end-start))
            if (height[start] < height[end]): #avoid being limitted by shortest line
                start += 1
            else:
                end -= 1
            
        return max_vol #this is an O(n) solution 
