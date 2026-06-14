# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = []
        current = head
        maxi = 0
        while current:
            result.append(current.val)  # Add the data
            current = current.next      # Move to the next node
            
        print(result)
        n = len(result)
        for i in range(n-1):
            cur = result[i] + result[n-1-i]
            maxi = max(cur, maxi)
            #maxi = cur
        return maxi
