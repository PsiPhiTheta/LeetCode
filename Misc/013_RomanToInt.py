class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_RomanToInt = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
 
        total = 0

        for i in range(0, len(s)-1):
            if (dict_RomanToInt[s[i]] < dict_RomanToInt[s[i+1]]):
                total -= dict_RomanToInt[s[i]]
            else:
                total += dict_RomanToInt[s[i]]
        
        total += dict_RomanToInt[s[len(s)-1]]
        
        return total
