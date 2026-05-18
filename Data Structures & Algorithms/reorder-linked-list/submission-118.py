# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        dummy = ListNode(None, head)
        
        fast, slow = head, dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l1, l2 = dummy.next, prev
        tail = dummy

        while l1 and l2:
            tmp1, tmp2 = l1.next, l2.next
            tail.next, tail.next.next = l1, l2
            l1, l2 = tmp1, tmp2
            tail = tail.next.next
        
        
