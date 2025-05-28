# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        def toarr(head):
            curr= head
            while curr:
                arr.append(curr.val)
                curr = curr.next
        def insert_end(root, item):
            temp = ListNode(item)
            if root is None:
                return temp

            last = root
            while last.next is not None:
                last = last.next
            
            last.next = temp
            return root
        def array_to_list(arr):
            root = None
            for item in arr:
                root = insert_end(root, item)
            return root
        toarr(list1)
        toarr(list2)
        arr.sort()
        root = array_to_list(arr)
        return root