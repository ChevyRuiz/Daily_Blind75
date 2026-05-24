class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Store in hashmap so that we have {index : Node}
        hashmap = dict()
        listLen = 0
        curr = head
        while curr:
            hashmap[listLen] = curr
            listLen += 1
            curr = curr.next
        # Store in stack
        stack = []
        i = 0
        while hashmap:
            stack.append(hashmap.pop(i))
            if hashmap:
                stack.append(hashmap.pop(listLen - (i + 1)))
            i += 1
        # Set the next pointer for each node
        for i in range(0, len(stack)):
            if i + 1 < len(stack):
                stack[i].next = stack[i + 1]
