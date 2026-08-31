# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_max_indices = []
        
        curr = head
        prev = curr.val
        curr = curr.next
        index = 1
        while curr and curr.next:
            if curr.val < prev and curr.val < curr.next.val:
                min_max_indices.append(index)
            elif curr.val > prev and curr.val > curr.next.val:
                min_max_indices.append(index)        

            index += 1
            prev = curr.val
            curr = curr.next
        print(min_max_indices)
        result = [-1, -1]
        if len(min_max_indices) < 2:
            return result
        min_distance = float('inf')

        for i in range(1, len(min_max_indices)):
            min_distance = min(min_distance, min_max_indices[i] - min_max_indices[i-1])

        max_distance = min_max_indices[-1] - min_max_indices[0]
        return [min_distance, max_distance]