def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    seen = set({})
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False

def tricky_hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head: return False

    slow,fast = head,head
    while slow.next and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
