class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if not m or not n: # deal with silly inputs
            return 0
        
        # Bot must move n-1 steps right + m-1 steps down (n+m-2 steps in total)
        # This can be done in any order.
        # e.g. if n=100 and m=99, need 99 steps right and 98 steps down, in any order
        
        # Using combinatorics (nCk) we have:
        # "If the set has n elements, the number of k-combinations is equal to":
        # N Choose K = N! / (K!)*(N-K)!
        # Here, N = (n+m-2), since we have (n+m-2) actions to take in any order 
        # Also, K = (n-1), since we can only chose (n-1) moments to turn right
        
        # Hence, we want: (n+m-2)! / ( (n-1)! * (n+m-2-(n-1))! ) = (n+m-2)! / ( (n-1)! * (m-1)! )
        
        ans = math.factorial(m+n-2)/ (math.factorial(n-1)*math.factorial(m-1))
        
        return ans
