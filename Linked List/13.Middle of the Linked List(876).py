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

    def middleNode_brute(self, head: [ListNode]) -> [ListNode]:
        temp = head
        len = 0
        while (temp != None):
            len += 1
            temp = temp.next
        desired = (len // 2) + 1
        temp = head
        while (temp != None):
            desired -= 1
            if (desired == 0):
                break
            temp = temp.next
        return temp

    def middleNode_optimal(self, head: [ListNode]) -> [ListNode]:
        slow = head
        fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().middleNode_brute(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,2,3,4,5,6])
head2 = Solution().middleNode_brute(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().middleNode_optimal(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,2,3,4,5,6])
head2 = Solution().middleNode_optimal(head1)
print(Solution().traversal(head2))

