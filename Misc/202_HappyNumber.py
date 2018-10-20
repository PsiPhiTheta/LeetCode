class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happy = n
        
        temp = [int(i) for i in str(n)]
        temp = sum(i*i for i in temp)
        if (happy == 7 or temp == 7): #since the only happy single digit number is 7
            return True
        
        while ((happy/10)>=1): #since all numbers eventually converge to a single digit
            digits = [int(i) for i in str(happy)]
            happy = sum(i*i for i in digits)
            
        if (happy == 1):
            return True
    
        else:
            return False
