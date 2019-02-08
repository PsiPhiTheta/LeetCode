from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        #Solution for biggest number in list order
        f = lambda a,b: 1 if a+b>b+a else -1 if a+b<b+a else 0
        n = map(str,nums)
        n = sorted(n, key=cmp_to_key(f), reverse=True)
        out = str(int("".join(n)))
        return out
        
        #Solution for biggest number in any order
        #i = ''.join(map(str, nums))
        #n = sorted(i, reverse=True)
        #n = ''.join(map(str, n))
        #return n
