# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        curr = head
        adj = curr.next
        adjHead = adj
        while curr.next != None and adj.next != None:
            curr.next = adj.next
            curr = curr.next
            adj.next = curr.next
            adj = adj.next
        curr.next = adjHead
        return head
