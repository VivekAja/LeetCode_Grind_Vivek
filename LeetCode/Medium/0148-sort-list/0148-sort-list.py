# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            print(slow.val)
        temp = slow.next
        print(f"Splitting at node with value: {slow.val}")
        print(f"Right half starts at: {temp.val if temp else 'None'}")
        slow.next = None

        left, right = self.sortList(head), self.sortList(temp)
        dummy = ListNode()
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        return dummy.next