# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        current = head
        
        # To list
        while current:
            result.append(current.val)  # Add the data
            current = current.next      # Move to the next node
            
        

        n = len(result)
        j = int(n/2)
        
        python_list = result[:j] + result[j+1:]
        if not python_list:
            return None
        head = ListNode(python_list[0])
        current = head
        
        # To Linked List
        for item in python_list[1:]:
            current.next = ListNode(item)  # Link new node
            current = current.next     # Move pointer forward
            
        return head