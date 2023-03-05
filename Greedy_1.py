# Minimum Swaps to Arrange a Binary Grid
# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        steps = 0
        N = len(grid)
        for i in range(N):
            if self.checker(i, i + 1, N, grid):
                continue
            for j in range(i + 1, N):
                if self.checker(j, i + 1, N, grid):
                    row_j = grid[j]
                    grid[i + 1:j + 1] = grid[i:j]
                    grid[i] = row_j
                    steps += j - i
                    break
                if j == N - 1:
                    return -1
        return steps

    @staticmethod
    def checker(row, pos, N, grid):
        for j in range(pos, N):
            if grid[row][j] != 0:
                return False
        return True


s = Solution()

assert (s.minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]) == 3)
assert (s.minSwaps([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]) == -1)
assert (s.minSwaps([[1, 0, 0], [1, 1, 0], [1, 1, 1]]) == 0)
assert (s.minSwaps([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]) == 2)
