# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        merged = ListNode()
        curr = merged 
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next
            elif curr1.val == curr2.val:
                 curr.next = curr1
                 curr1 = curr1.next
                 curr = curr.next
                 curr.next = curr2
                 curr2 = curr2.next
                 curr = curr.next
            elif curr1.val > curr2.val:
                 curr.next = curr2
                 curr2 = curr2.next
                 curr = curr.next
        if curr1==None:
            while curr2:
                curr.next = curr2
                curr2 = curr2.next
                curr = curr.next
        else:
            while curr1:
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next
        if list1==None:
            return list2
        elif list2==None:
            return list1
        return merged.next



        
        