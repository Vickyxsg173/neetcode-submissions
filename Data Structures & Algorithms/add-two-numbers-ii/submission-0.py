# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        num1 = ""
        num2 = ""
        curr = head1
        curr2 = head2
        while curr:
            num1 += str(curr.val)
            curr = curr.next

        while curr2:
            num2 += str(curr2.val)
            curr2=curr2.next

        sumf = int(num1) + int(num2)
        s = str(sumf)
        head = ListNode(s[0])
        current = head
        for i in s[1:]:
            current.next = ListNode(i)
            current = current.next

        return head




