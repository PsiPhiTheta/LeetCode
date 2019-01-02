class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #matrix.reverse()
        
        n = len(matrix)
        
        print(matrix)
        
        matrix.reverse()
        
        print(matrix)
                
        for i in range(0,n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
        print(matrix)
