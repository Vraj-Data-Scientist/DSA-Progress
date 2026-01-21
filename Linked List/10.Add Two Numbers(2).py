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

    def addTwoNumbers(self, l1:[ListNode], l2:[ListNode]) -> [ListNode]:
        dummy_head = ListNode(-1)
        t1 = l1
        t2 = l2
        curr = dummy_head
        carry = 0
        while (t1 != None or t2 != None):
            sum = carry
            if (t1): sum += t1.val
            if (t2): sum += t2.val
            new = ListNode(sum % 10)
            carry = sum // 10
            curr.next = new
            curr = curr.next
            if (t1):
                t1 = t1.next
            if (t2):
                t2 = t2.next
        if (carry):
            new = ListNode(carry)
            curr.next = new
        return dummy_head.next

head1 = Solution().arr_to_LL([9,9,9,9,9,9,9])
head2 = Solution().arr_to_LL([9,9,9,9])
head3 = Solution().addTwoNumbers(head1, head2)
print(Solution().traversal(head3))


