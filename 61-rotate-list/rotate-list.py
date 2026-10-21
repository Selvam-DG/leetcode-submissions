# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
            
        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next
        curr.next = head
        temp = head
        k = k % length
        for _ in range(length-k-1):
            temp = temp.next
        head = temp.next
        temp.next = None

        return head
