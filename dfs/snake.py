s_map = [
    [8, 7, 7, 8, 2, 8, 2, 0, 5, 5],
    [1, 3, 0, 4, 6, 2, 8, 2, 8, 4],
    [4, 4, 'V', 'V', 3, 'V', 'V', 4, 2, 0],
    [0, 6, 'V', 'V', 9, 'V', 'V', 3, 4, 3],
    [6, 0, 'V', 'V', 'V', 'V', 'V', 6, 2, 1],
    [2, 2, 'V', 4, 'V', 'V', 'V', 5, 4, 5],
    [7, 6, 'V', 6, 2, 5, 'V', 2, 1, 1],
    [2, 8, 'V', 5, 2, 9, 'S', 6, 8, 4],
    [1, 5, 9, 5, 0, 2, 2, 4, 5, 1],
    [6, 2, 9, 2, 6, 1, 2, 0, 9, 2]]

from typing import List
from copy import deepcopy


class SnakeSolution:
    def __init__(self, s_map: List[List[int]], power):
        self.s_map = s_map
        self.power = power
        self.max = 0

    # dfs
    def optimal_path(self):
        s_map = self.s_map
        height = len(s_map)
        width = len(s_map[0])
        start_point = 0, 0
        for i in range(height):
            for j in range(width):
                if s_map[i][j] == 'S':
                    start_point = i, j
        length = 0

        def dfs(s_map, cur_point, power, length):
            if s_map[cur_point[0]][cur_point[1]] != 'S':
                power -= s_map[cur_point[0]][cur_point[1]]
                s_map[cur_point[0]][cur_point[1]] = 'V'
                if power < 0:
                    self.max = max(length, self.max)
                    return length
                length += 1
            else:
                s_map[cur_point[0]][cur_point[1]] = 'V'

            if cur_point[0] + 1 < height:
                next_point = cur_point[0] + 1, cur_point[1]
                if s_map[next_point[0]][next_point[1]] != 'V':
                    dfs(deepcopy(s_map), next_point, power, length)
            if cur_point[0] - 1 >= 0:
                next_point = cur_point[0] - 1, cur_point[1]
                if s_map[next_point[0]][next_point[1]] != 'V':
                    dfs(deepcopy(s_map), next_point, power, length)
            if cur_point[1] + 1 < width:
                next_point = cur_point[0], cur_point[1] + 1
                if s_map[next_point[0]][next_point[1]] != 'V':
                    dfs(deepcopy(s_map), next_point, power, length)
            if cur_point[1] - 1 >= 0:
                next_point = cur_point[0], cur_point[1] - 1
                if s_map[next_point[0]][next_point[1]] != 'V':
                    dfs(deepcopy(s_map), next_point, power, length)

        dfs(s_map, start_point, power=self.power, length=length)
        return self.max


if __name__ == '__main__':
    length = SnakeSolution(s_map=s_map, power=42).optimal_path()
    print(length)
