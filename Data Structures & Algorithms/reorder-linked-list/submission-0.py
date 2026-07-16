# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(h):
            curr=h
            prev=None
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        def mid(h):
            fast=h
            slow=h
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        mid_ele=mid(head)
        new_head=mid_ele.next
        mid_ele.next=None
        new_head=reverse(new_head)
        curr1=head
        curr2=new_head
        while curr1 and curr2:
            nxt1=curr1.next
            nxt2=curr2.next
            curr1.next=curr2
            curr2.next=nxt1
            curr1=nxt1
            curr2=nxt2
        

        
        