class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = []
        pascal_row = [None]*(rowIndex+1)
        
        for i in range(rowIndex+1):
            pascal.append([1]*(i+1))
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        for k in range(rowIndex+1):
            pascal_row[k] = pascal[rowIndex][k] 
        
        return pascal_row
