Iterative:
#Time: O(n) 
#Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        prev_nonexistantNode = None

        while curr:
            upcomingNode = curr.next

            curr.next = prev_nonexistantNode

            prev_nonexistantNode = curr

            curr = upcomingNode
        
        return prev_nonexistantNode


Recursive:
# TC: O(n) 
# Space: O(n) 
    def reverseList(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head












        
