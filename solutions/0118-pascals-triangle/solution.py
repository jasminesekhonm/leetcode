class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        output = [[1], [1, 1]]
        if numRows == 2:
            return output
        
        for i in range(3, numRows+1):
            output_ = [1 for _ in range(i)]
            # n -> n, n -1
            for j in range(len(output_)):
                if j != 0 and j != (len(output_) - 1):
                    output_[j] = output[-1][j] + output[-1][j-1]
            output.append(output_)
        return output
        
