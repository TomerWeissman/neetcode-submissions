
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        first, second = head, prev

        while second:
            tmps = second.next
            tmpf = first.next

            first.next = second
            second.next = tmpf

            second = tmps
            first = tmpf
        



        