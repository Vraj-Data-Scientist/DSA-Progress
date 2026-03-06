class Solution:
    def solve_brute(self, maze, n, visited, move, res, i, j):
        if (i == n-1 and j == n-1):
            res.append(move)
            return
        # downward
        if (i+1 < n and not visited[i+1][j] and maze[i+1][j] == 1):
            visited[i][j] = 1
            self.solve_brute(maze, n, visited, move + "D", res, i+1, j)
            visited[i][j] = 0
        # left
        if (j-1 >= 0 and not visited[i][j-1] and maze[i][j-1] == 1):
            visited[i][j] = 1
            self.solve_brute(maze, n, visited, move + "L", res, i, j-1)
            visited[i][j] = 0
        # right
        if (j+1 < n and not visited[i][j+1] and maze[i][j+1] == 1):
            visited[i][j] = 1
            self.solve_brute(maze, n, visited, move + "R", res, i, j+1)
            visited[i][j] = 0
        # upward
        if (i-1 < n and not visited[i-1][j] and maze[i-1][j] == 1):
            visited[i][j] = 1
            self.solve_brute(maze, n, visited, move + "U", res, i-1, j)
            visited[i][j] = 0

    def find_path_brute(self, maze, n):
        res = []
        move = ""
        visited = [[0] * n for _ in range(n)]
        if maze[0][0] == 1:
            self.solve_brute(maze, n, visited, move, res, 0, 0)
        return res









maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
n = len(maze)
print(Solution().find_path_brute(maze, n))