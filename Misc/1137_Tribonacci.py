class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        
        else:
        # Solution 2. Recursive solution
            # fib = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            # return fib

        # Solution 3. Dp solution (faster than recursive, takes memory)
            fib = [0,1,1]
            for i in range(3,n+1):
                fibi=fib[i-1]+fib[i-2]+fib[i-3]
                fib.append(fibi)
            return fib[n]
