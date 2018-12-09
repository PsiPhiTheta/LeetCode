class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = []
        
        for l in letters:
            if (s.count(l) == 1):
                index.append(s.index(l))
        
        if (len(index) > 0):
            return min(index)  
        else:
            return -1
