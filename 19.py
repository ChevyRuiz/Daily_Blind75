# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        if length <= 1:
            return None

        index = length - n

        if index == 0:
            return head.next

        curr = head
        for i in range(1, index):
            curr = curr.next

        curr.next = curr.next.next
        return head
