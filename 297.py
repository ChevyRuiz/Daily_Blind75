# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[N]"

        q = deque([root])
        result = []

        while q:
            curr = q.popleft()

            if curr is None:
                result.append("[N]")
            else:
                result.append("[" + str(curr.val) + "]")
                q.append(curr.left)
                q.append(curr.right)

        return "".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "[N]":
            return None

        nums = data.strip("[]").split("][")

        root = TreeNode(int(nums[0]))
        q = deque([root])

        i = 1

        while q and i < len(nums):
            curr = q.popleft()

            # Left child
            if nums[i] != "N":
                curr.left = TreeNode(int(nums[i]))
                q.append(curr.left)

            i += 1

            # Right child
            if i < len(nums) and nums[i] != "N":
                curr.right = TreeNode(int(nums[i]))
                q.append(curr.right)

            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
