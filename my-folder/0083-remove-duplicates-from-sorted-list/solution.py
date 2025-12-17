# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        prev = head
        curr = head.next
        while True:
            if curr.val == prev.val:
                if curr.next is not None:
                    curr = curr.next
                else:
                    prev.next = None
                    return head
            else:
                prev.next = curr
                prev = curr
                if curr.next is not None:
                    curr = curr.next
                else:
                    return head
