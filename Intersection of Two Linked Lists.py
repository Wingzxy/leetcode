# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        S = set()
        while headA != None: headA, _ = headA.next, S.add(headA)
        while headB != None:
            if headB in S: return headB
            headB = headB.next
