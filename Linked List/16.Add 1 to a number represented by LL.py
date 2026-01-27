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

    def reverseList(self, head: [ListNode]) -> [ListNode]:
        temp = head
        prev = None
        while (temp != None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def add_1_number(self, head: [ListNode]) -> [ListNode]:
        head = Solution().reverseList(head)
        temp = head
        carry = 1
        while (temp != None):
            sum = (temp.val + carry) % 10
            carry = (temp.val + carry) // 10
            temp.val = sum
            temp = temp.next
        if (carry):
            new = ListNode(carry)
            head = Solution().reverseList(head)
            new.next = head
            return new
        head = Solution().reverseList(head)
        return head

    def helper_return_carry(self, head: [ListNode]) -> [ListNode]:
        temp = head
        if (temp == None):
            return 1
        carry = Solution().helper_return_carry(temp.next)
        sum = (temp.val + carry) % 10
        carry = (temp.val + carry) // 10
        temp.val = sum
        return carry

    def add_1_number_recursive(self, head: [ListNode]) -> [ListNode]:
        carry = Solution().helper_return_carry(head)
        if (carry):
            new = ListNode(carry, head)
            return new
        return head



head1 = Solution().arr_to_LL([9,9,9,9])
head2 = Solution().add_1_number(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,5,9])
head2 = Solution().add_1_number(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([9,9,9,9])
head2 = Solution().add_1_number_recursive(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,5,9])
head2 = Solution().add_1_number_recursive(head1)
print(Solution().traversal(head2))
