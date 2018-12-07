class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)
        
        s_list.sort()
        t_list.sort()
        
        if (s_list == t_list):
            return True
        else:
            return False
