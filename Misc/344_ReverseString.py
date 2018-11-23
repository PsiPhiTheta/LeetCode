class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = list(s)
        output = output[::-1]
        output = "".join(output)
        return output
        
