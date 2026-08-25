# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev_node = None
        # 0 -> 1 | 1 -> 2 | 2 -> 3 | 3 -> None
        while curr:
            next_node = curr.next
            
            curr.next = prev_node    
            prev_node = curr         
            curr = next_node         

        return prev_node
