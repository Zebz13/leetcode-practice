class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        rows = len(box)
        cols = len(box[0]) #lower limit is 1
        output_box = [['.'] * rows for _ in range(cols)]
        for index_row,box_row in enumerate(box):
            compare_point = cols-1
            for index_col in range(cols-1,-1,-1):
                if(box[index_row][index_col] == '*'):
                    output_box[index_col][rows-index_row-1] = '*'
                    compare_point=index_col-1
                elif(box[index_row][index_col] == '#'):
                    if compare_point>index_col:
                        output_box[compare_point][rows-index_row-1] = '#'
                        output_box[index_col][rows-index_row-1] = '.'
                        compare_point-=1
                    else:
                        output_box[index_col][rows-index_row-1] = '#'
                        compare_point-=1
        return output_box
sol = Solution()
print(sol.rotateTheBox([["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]))