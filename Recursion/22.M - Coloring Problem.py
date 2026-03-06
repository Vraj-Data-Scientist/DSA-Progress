class Solution:
    def is_safe(self, graph, m, n, node, color_ds, color):
        for k in range(n):
            if k != node and graph[k][node] == 1 and color_ds[k] == color:
                return False
        return True

    def solve(self, graph, m, n, node, color_ds):
        if (node == n):
            return True
        for i in range(1, m+1):
            if (self.is_safe(graph, m, n, node, color_ds, i)):
                color_ds[node] = i
                if self.solve(graph, m, n, node+1, color_ds):
                    return True
                color_ds[node] = 0
        return False

    def graph_coloring(self, graph, m, n):
        color_ds = [0] * n
        if self.solve(graph, m, n, 0, color_ds):
            return True
        return False


N = 4
m = 3
# Sample graph with edges (0,1), (1,2), (2,3), (3,0), (0,2)
graph = [[False] * 101 for _ in range(101)]
graph[0][1] = graph[1][0] = True
graph[1][2] = graph[2][1] = True
graph[2][3] = graph[3][2] = True
graph[3][0] = graph[0][3] = True
graph[0][2] = graph[2][0] = True
print(graph)

print(Solution().graph_coloring(graph, 2,4))