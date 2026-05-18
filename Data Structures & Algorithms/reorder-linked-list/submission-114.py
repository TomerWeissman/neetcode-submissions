# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        dummy = ListNode(0, head)
        
        slow, fast = dummy, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prv = slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt
        
        l1, l2 = dummy.next, prv
        tail = dummy
        
        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            tail.next = l1
            tail.next.next = l2
            tail = tail.next.next
            l1, l2 = tmp1, tmp2
        
        




        