class Solution:
    def reverseBits(self, n):
        '''
        input: n, an integer
        return: an integer
        '''
        n = format(n, '032b')
        n = list(str(n))
        n = n[::-1]

        n = int(''.join(map(str,n)))
        n = str(n)
        n = int(n, 2)
        
        return n
