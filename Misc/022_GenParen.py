class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        s = [("(", 1, 0)] # must always start with one rhs parenthesis
        
        while s:
            print(s)
            x, lhs, rhs = s.pop()
            print(x, lhs, rhs)

            if (lhs - rhs < 0) or (lhs > n) or (rhs > n): # if invalid then reloop & pop
                continue
            if (lhs == n) and (rhs == n): # if valid then append to ans
                ans.append(x)
            s.append((x+"(", lhs+1, rhs))
            s.append((x+")", lhs, rhs+1))
        return ans
