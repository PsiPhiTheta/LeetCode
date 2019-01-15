class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if (len(needle) == 0):
            return 0
        
        if (needle in haystack):
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i] != needle[0]:
                    continue
                if haystack[i:i+len(needle)] == needle:
                    return i
        else:
            return -1
