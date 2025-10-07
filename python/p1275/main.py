from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        x_moves = []
        o_moves = []
        for idx, move in enumerate(moves):
            if idx % 2 == 0:
                x_moves.append(move)
            else:
                o_moves.append(move)

        dirs = [[1, 0], [1, 1], [0, 1], [-1, 1]]
        for dir in dirs:
            is_x_win = self.walk_moves(sorted(x_moves), dir)
            if is_x_win:
                return "A"

            is_o_win = self.walk_moves(sorted(o_moves), dir)
            if is_o_win:
                return "B"

        return "Draw" if len(moves) == 9 else "Pending"

    def walk_moves(self, moves, dir):
        for move in moves:
            is_wins = self.r_walk_moves(moves, dir, move, 0)
            if is_wins:
                return True

        return False

    def r_walk_moves(self, moves, dir, init_pos, num_in_row):
        if num_in_row == 3:
            return True

        curr_pos = [
                (num_in_row * v + init_pos[i])
                for i, v in enumerate(dir)
            ]
        print(curr_pos)
        if curr_pos not in moves:
            return False

        return self.r_walk_moves(moves, dir, init_pos, num_in_row + 1)
