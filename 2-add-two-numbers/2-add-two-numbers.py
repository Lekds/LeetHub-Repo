# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode()
        b = a
        nextcarry = 0
        while l1 or l2 or nextcarry:
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0
            val =  value_1 + value_2 +nextcarry
            nextcarry = val//10
            val = val%10
            b.next = ListNode(val)
            b = b.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return a.next