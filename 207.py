class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node, matrix, visited, pathVisited):
            if pathVisited[node]:
                return True

            if visited[node]:
                return False

            visited[node] = pathVisited[node] = True

            for nei in range(len(matrix)):
                if matrix[node][nei] == 1:
                    if  dfs(nei, matrix, visited, pathVisited):
                        return True
            pathVisited[node] = False
            return False


        # Create adjacency matrix
        rows = cols = numCourses
        matrix = [[0 for _ in range(cols)] for _ in range(rows)] 
        visited = [False] * numCourses
        pathVisited = [False] * numCourses

        # Fill in adjacency matrix
        for prereq in prerequisites:
            matrix[prereq[1]][prereq[0]] = 1

        # DFS to detect cycle
        for node in range(numCourses):
            if dfs(node, matrix, visited, pathVisited):
                return False
        return True
        
