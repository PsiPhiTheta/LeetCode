class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        out = 1
        
        if (n < 0):
            x = 1/x
            n = -n
        
        while n:
            if (n % 2):
                out *= x
            x *= x
            n >>= 1
            
        return out # this is the iterative solution
