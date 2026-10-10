class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i])-1
            while l<=r:
                middle = l+(r-l)//2
                if target>matrix[i][middle]:
                    l = middle+1
                elif target<matrix[i][middle]:
                    r = middle-1
                elif target == matrix[i][middle]:
                    return True
        return False


        