class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]: 

        def dfs(node, visited, heights, prevHeight):
            ROWS = len(heights)
            COLS = len(heights[0])
            

            if node[0] < 0 or  node[0] >= ROWS or node[1] < 0 or node[1] >= COLS or node in visited:
                return
            
            height = heights[node[0]][node[1]]

            if height < prevHeight:
                return
            
            visited.add(node)
            dfs((node[0] + 1, node[1]),visited, heights, height)
            dfs((node[0] - 1, node[1]),visited, heights, height)
            dfs((node[0], node[1] + 1),visited, heights, height)
            dfs((node[0], node[1] - 1),visited, heights, height)

        pacificSet = set()
        pacificVisited = set()
        atlanticSet = set()
        atlanticVisited = set()

        ROWS = len(heights)
        COLS = len(heights[0])
        
        for i in range(ROWS):
            pacificSet.add((i, 0))
            atlanticSet.add((i, COLS - 1))

        for j in range(COLS):
            pacificSet.add((0, j))
            atlanticSet.add((ROWS - 1, j))

        for node in pacificSet:
            dfs(node, pacificVisited, heights, -1)
        for node in atlanticSet:
            dfs(node, atlanticVisited, heights, -1)
        

        return [list(node) for node in pacificVisited & atlanticVisited]
