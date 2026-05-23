"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        # DFS
        stack = []
        seen = set()
        stack.append(node)
        while stack:
            curr = stack.pop()
            if(curr not in seen):
                seen.add(curr)
            for n in curr.neighbors:
                if(n not in seen):
                    stack.append(n)

        # Copy
        hashmap = dict()
        for ogNode in seen:
            if ogNode.val in hashmap:
                copyNode = hashmap[ogNode.val]
            else:
                copyNode = Node(ogNode.val, [])
                hashmap[ogNode.val] = copyNode
            for n in ogNode.neighbors:
                if n.val not in hashmap:
                    nCopy = Node(n.val, [])
                    hashmap[n.val] = nCopy
                copyNode.neighbors.append(hashmap[n.val])
        if hashmap:
            return hashmap[node.val]
        else:
            return None
