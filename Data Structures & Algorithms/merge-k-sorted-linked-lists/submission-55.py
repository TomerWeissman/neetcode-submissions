# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #edge cases
        if not lists or len(lists) == 0:
            return None
        

        #Merge Function

        def merge(l1, l2):

            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            if l1:
                tail.next = l1
            else:
                tail.next = l2
            
            return dummy.next



        #---
        #while len(lists) > 1:
        while len(lists) > 1:
            ans = []
            #for loop -> jump two each time
            for i in range(0, len(lists), 2):

                #If there is a next one merge with that, if not merge with None
                l1 = lists[i]
                if i+1 > len(lists) - 1:
                    l2 = None
                else:
                    l2 = lists[i+1]
                
                #append to ans
                ans.append(merge(l1, l2))
            
            #lists = ans
            lists = ans

        #return total
        return lists[0]
