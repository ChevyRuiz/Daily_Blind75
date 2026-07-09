"""
        def dfs(node, nUniquePaths):
            # Base case

            # B1: path that leads to grid[m - 1][n - 1]
            if node == [m - 1, n - 1]:
                nUniquePaths[0] = nUniquePaths[0] + 1
                return
            # B2: path that leads nowhere
            if node[0] >= m or node[1] >= n:
                return 

            # Recursive case

            # R1: go down
            dfs([node[0] + 1, node[1]], nUniquePaths)

            # R2: go right
            dfs([node[0], node[1] + 1], nUniquePaths)


        nUniquePaths = [0]
        dfs([0,0], nUniquePaths)
        return nUniquePaths[0]
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m -1):
            newRow = [1] * n
            for j in range(n -2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
