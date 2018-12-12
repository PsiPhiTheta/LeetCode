class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        if (n < 3):
            # Special cases
            # 0 = 0:
            # 1 = 1: 1
            # 2 = 2: 2, 1 1
            return n
        
        else: # Fibonaci from here onward
            # 3 = 3: 1 1 1, 2 1, 1 2
            # 4 = 5: 1 1 1 1, 2 1 1, 1 2 1, 1 1 2, 2 2  
            # 5 = 8: 1 1 1 1 1, 2 1 1 1, 1 2 1 1 , 1 1 2 1, 1 1 1 2, 2 2 1, 1 2 2, 2 1 2
            # 6 = 13: 1 1 1 1 1 1, 2 1 1 1 1, 1 2 1 1 1, 1 1 2 1 1, 1 1 1 2 1, 1 1 1 1 2, 
            # Fibonaci pattern spotted as shown above... 
            preprev = 1 # Resume from special cases
            prev = 2 # Resume from special cases
    
            for i in range(n-2): # omit the first two steps
                temp = preprev
                preprev = prev # update preprev for next iter
                prev = prev + temp # update prev for next iter
                
            return prev
