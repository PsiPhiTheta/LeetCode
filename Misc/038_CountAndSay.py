class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        out = '1'
        for _ in range(n-1):
            nxt, temp, count = out[0], '', 0
            for l in out:
                if nxt == l:
                    count += 1
                else:
                    temp += str(count)+nxt
                    nxt = l
                    count = 1
            temp += str(count)+nxt
            out = temp
        return out
