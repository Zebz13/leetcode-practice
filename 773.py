class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        string_board = "".join([str(cell) for row in board for cell in row])
        look_up_view={
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }

        history_visits = set()
        paths_to_check = [(string_board,string_board.index('0'),0)] #put current board,index of 0 and number of steps
        while paths_to_check:
            string_board,index_of_zero,path_length = paths_to_check.pop(0)
            if(string_board == '123450'):
                return path_length
            
            string_arr = list(string_board)

            for next_step in look_up_view[index_of_zero]:
                temp_arr = string_arr.copy()
                temp_arr[index_of_zero],temp_arr[next_step] = string_arr[next_step],string_arr[index_of_zero]
                back_to_string = "".join(temp_arr)
                if(back_to_string not in history_visits):
                    paths_to_check.append((back_to_string,back_to_string.index('0'),path_length+1))
                    history_visits.add(back_to_string)
        return -1

sol = Solution()
print(sol.slidingPuzzle([[4,1,2],[5,0,3]]))