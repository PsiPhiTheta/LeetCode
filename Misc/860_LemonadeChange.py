class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change5 = 0
        change10 = 0
        
        for i in bills:
            if (i == 5):
                change5 += 1
            if (i == 10):
                if (change5 > 0):
                    change5 -= 1
                    change10 += 1
                else:
                    return False
            if (i == 20): 
                if (change10 > 0 and change5 > 0):
                    change10 -= 1
                    change5 -= 1
                else:
                    if (change5 > 2):
                        change5 -= 3
                    else:
                        return False
        return True
