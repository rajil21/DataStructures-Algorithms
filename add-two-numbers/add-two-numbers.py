# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        s2 = ""
        while l1:
            s1 = str(l1.val) + s1
            l1 = l1.next
        while l2:
            s2 = str(l2.val) + s2
            l2 = l2.next
        s = str(int(s1) + int(s2))
        int_list = [int(i) for i in s]
        int_list.reverse()
        if int_list:
            head = ListNode(int_list[0])
            tail = head
            for i in range(1, len(int_list)):
                head.next = ListNode(int_list[i])
                head = head.next
                
            return tail
        else:
            return ListNode()