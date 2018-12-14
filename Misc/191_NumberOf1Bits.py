class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = "{0:b}".format(n)
        lst = [int(d) for d in str(n)]

        return sum(lst)
