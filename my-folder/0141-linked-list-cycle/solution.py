# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Tortoise-Hare algorithm (slow and fast pointers)
        # if there is a cycle, they will cross paths eventually
        # else fast will reach null node and exit
        if head is None:
            return False

        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

        
