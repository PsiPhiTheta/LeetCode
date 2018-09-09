class Solution:
    def addDigits(self, num):
        total = 0 
        
        while num >= 10:
            digits = [int(x) for x in str(num)]
            num = sum(digits)
        
        return num
            
