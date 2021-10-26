lass Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        
        else:
            # Solution 1. Fastest
            # fib30 = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040]
            # return fib30[n]
            
            # Solution 2. Recursive solution
            # fib = self.fib(n-1) + self.fib(n-2)
            # return fib

            # Solution 3. Dp solution (faster than recursive, takes memory)
            fib = [0,1]
            for i in range(2,n+1):
                fibi=fib[i-1]+fib[i-2]
                fib.append(fibi)
            return fib[n]
            
