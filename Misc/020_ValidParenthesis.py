class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        length = len(s)
        
        if (length == 0): # Deal with fringe case
            return True
        
        if (length%2 != 0): # Remove obvious mismatches early
            return False
        
        while '()' in s or '{}' in s or '[]' in s: # Simplify the string
            s = s.replace('{}','')
            s = s.replace('()','')
            s = s.replace('[]','')
        
        if (len(s) == 0): # If 0, valid. Else invalid (1).
            return True
        else:
            return False
