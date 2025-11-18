class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        triangle.append([])
        triangle.append([1])
        if numRows == 1:
            return triangle[1:]
        triangle.append([1,1])
   
        for row in range(3, numRows+1):
            lst = [1] * row
            for col in range(1, row-1):
                lst[col] = triangle[row-1][col-1] + triangle[row-1][col]
            triangle.append(lst)
        return triangle[1:]


        
