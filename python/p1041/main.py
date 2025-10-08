class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        init_dir = [0, 1]
        pos = [0, 0]

        dir = init_dir
        for instruction in instructions:
            if instruction == "G":
                pos = [pos[i] + d for i, d in enumerate(dir)]
            elif instruction == "L":
                dir = [-dir[1], dir[0]]
            elif instruction == "R":
                dir = [dir[1], -dir[0]]

        if init_dir == dir and pos != [0, 0]:
            return False

        return True
