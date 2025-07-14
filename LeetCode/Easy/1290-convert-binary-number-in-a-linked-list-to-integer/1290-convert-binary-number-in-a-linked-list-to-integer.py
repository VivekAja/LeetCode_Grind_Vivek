# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        
        print(arr)
        n = len(arr)
        val, i, j  = 0, n-1, 1
        #arr.sort(reverse= True)
        for j in arr:
            val += j * (2** i)
            i-=1
        print(val)
        return val
