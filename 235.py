# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node, val, pathStack):
            if not node:
                return

            pathStack.append(node)
            if val < node.val:
                find(node.left, val, pathStack)
            elif val > node.val:
                find(node.right, val, pathStack)
            else:
                return

        pathP = []
        pathQ = []
        find(root, p.val, pathP)
        find(root, q.val, pathQ)
        pathQ = set(pathQ)
        
        while pathP:
            lastElement = pathP.pop()
            if lastElement in pathQ:
                return lastElement
        return None
