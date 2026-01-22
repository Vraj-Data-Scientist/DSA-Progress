class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def arr_to_LL(self, arr):
        n = len(arr)
        head = ListNode(arr[0])
        mover = head
        for i in range(1, n):
            temp = ListNode(arr[i])
            mover.next = temp
            mover = temp
        return head

    def traversal(self, head):
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.next

    def removeNthFromEnd_brute(self, head: [ListNode], n: int) -> [ListNode]:
        len = 0
        temp = head
        while (temp != None):
            len += 1
            temp = temp.next
        desired_pos = len - n
        if (desired_pos == 0):
            return head.next
        temp = head
        while (temp != None):
            desired_pos -= 1
            if (desired_pos == 0):
                break
            temp = temp.next
        front = temp.next
        temp.next = temp.next.next
        front = None
        return head

    def removeNthFromEnd_optimal(self, head: [ListNode], n: int) -> [ListNode]:
        slow = head
        fast = head
        for i in range(0, n):
            fast = fast.next
        if (fast == None):
            return head.next
        while (fast.next != None):
            fast = fast.next
            slow = slow.next
        front = slow.next
        slow.next = slow.next.next
        front = None
        return head



head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().removeNthFromEnd_brute(head1, 1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().removeNthFromEnd_optimal(head1, 5)
print(Solution().traversal(head2))

