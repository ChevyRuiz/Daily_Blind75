class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def hasCycle(node, visited, parent, matrix):

            # Mark the current node as visited
            visited.add(node)

            # Go through all nodes adjacent to the current node
            for adj in [i for i in range(len(matrix[node])) if matrix[node][i] == 1]:

                # If we haven't visited the adjacent node yet,
                # perform DFS starting from that node
                if adj not in visited:
                    if hasCycle(adj, visited, node, matrix):
                        return True  # A cycle was found deeper in the DFS

                # If the adjacent node was already visited and it is NOT
                # the node we just came from (the parent), we found a cycle
                elif adj != parent:
                    return True

            # Finished exploring this node without finding a cycle
            return False

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        # Build adjecency matrix
        for edge in edges:
            matrix[edge[0]][edge[1]] = 1
            matrix[edge[1]][edge[0]] = 1
        
        visited = set()

        # DFS to detect cycle starting from node 0
        if hasCycle(0, visited, -1, matrix):
            return False # If there is a cycle, return False

        # Check also that all the nodes are connected as one componenent
        return True and len(visited) == n
