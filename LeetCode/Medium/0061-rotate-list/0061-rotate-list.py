# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        n = len(arr)
        k%=n
        if k == 0: return head
        rotated = arr[n-k:] + arr[:n-k]
        print(rotated)
        naya = ListNode(rotated[0])
        curr = naya

        for i in range(1, n):
            curr.next = ListNode(rotated[i])
            curr = curr.next
        return naya
        