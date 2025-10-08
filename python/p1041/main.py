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
                print(f"changing dir: {dir}")
            elif instruction == "R":
                dir = [dir[1], -dir[0]]
                print(f"changing dir: {dir}")

        if init_dir == dir:
            print(f"init_dir: {init_dir} -- dir: {dir}")
            return False

        return True
