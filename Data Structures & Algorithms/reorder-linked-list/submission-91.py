# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val)
        
        curr = slow.next
        prv = slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt
        
        l1 = head
        l2 = prv
        
        
        
        dummy = ListNode(None)
        tail = dummy

        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            tail.next = l1
            tail.next.next = l2
            l1 = tmp1
            l2 = tmp2
            tail = tail.next.next
        
        if l1:
            tail.next = l1

        
        


        