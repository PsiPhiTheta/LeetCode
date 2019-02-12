class Solution:
    def numSquares(self, n: 'int') -> 'int':
        
        # Step 0. Deal with silly inputs
        if n < 2: 
            return n
        
        # Step 1. Generate all the perfect squares
        lst = []
        i = 1
        while (i**2<= n): # include n in case solution of 1 exists
            lst.append(i**2)
            i += 1
            
        # Step 2. Find the least number of those that sum to n (BFS)
        cnt = 0
        toCheck = {n} # dicts save time for processing duplicate nums on same lvl
        while toCheck:
            cnt += 1
            temp = set() # reset the set
            for x in toCheck:
                for y in lst:
                    #print(x, y, temp, cnt)
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp # update toCheck with next vals, loop back

        return cnt
