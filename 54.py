class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        visited = set()
        ROWS = len(matrix)
        COLS = len(matrix[0])
        extraCount = 0
        ans = []
        for i in range(ROWS):
            visited.add((i, COLS))
            visited.add((i, -1))
            extraCount += 2
        for i in range(COLS):
            visited.add((ROWS, i))
            extraCount += 1
        
        currDirection = 0
        curr = (0, 0)
        while len(visited) < ROWS*COLS + extraCount:
            ans.append(matrix[curr[0]][curr[1]])
            visited.add(curr)
            direction = directions[currDirection]
            if (curr[0] + direction[0], curr[1] + direction[1]) in visited:
                currDirection = (currDirection + 1) % 4
                direction = directions[currDirection]
            curr = (curr[0] + direction[0], curr[1] + direction[1])
        return ans
