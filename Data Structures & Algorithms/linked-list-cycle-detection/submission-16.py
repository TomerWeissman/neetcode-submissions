# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        fast = slow = head

        while fast:
            if not fast.next or not fast.next.next:
                return False
            
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False