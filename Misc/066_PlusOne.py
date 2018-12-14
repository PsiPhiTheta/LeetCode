class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total = 0
        
        for i in range(len(digits)):
            total += digits[i]*(10**(len(digits)-i-1))
            
        print (total)
        
        total += 1
        
        total = [int(d) for d in str(total)]
        
        print (total)
        
        return total
