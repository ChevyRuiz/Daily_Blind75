class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, visited, matrix):
            # Base case
            if node in visited:
                return
            # Recursive case
            visited.add(node)
            for adj in [i for i in range(len(matrix[node])) if matrix[node][i] == 1]:
                dfs(adj, visited, matrix)
            
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        count = 0
        visited = set()
        # Build adjecency matrix
        for edge in edges:
            matrix[edge[0]][edge[1]] = 1
            matrix[edge[1]][edge[0]] = 1
        
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node, visited, matrix)
        
        return count
