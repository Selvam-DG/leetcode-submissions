# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        result = ListNode(0)
        temp = result
        add = 0
        carry = 0
        while l1 or l2:
            add = carry + (l1.val if l1 else 0)  +( l2.val if l2 else 0)
            temp.next = ListNode(add % 10)
            carry = add // 10

            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        
        return result.next

