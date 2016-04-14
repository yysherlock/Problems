# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head: return head
        
        num = 1
        odd,even = head, head.next
        evenhead = head.next
        cur = head

        while cur:
            if num % 2:
                if not num == 1:
                    odd.next = cur
                    odd = cur
            else:
                if not num==2:
                    even.next = cur
                    even = cur

            cur = cur.next
            num += 1

        odd.next = evenhead

        if even: even.next = None

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
result = oddEvenList(head)
while result:
    print result.val
    result = result.next
