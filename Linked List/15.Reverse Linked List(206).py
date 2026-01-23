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

    def reverseList_brute(self, head: [ListNode]) -> [ListNode]:
        stack = []
        temp = head
        while (temp != None):
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while (temp != None):
            temp.val = stack[-1]
            stack.pop()
            temp = temp.next
        return head

    def reverseList_optimal_iterative(self, head: [ListNode]) -> [ListNode]:
        prev = None
        temp = head
        while (temp != None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev


head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().reverseList_brute(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().reverseList_optimal_iterative(head1)
print(Solution().traversal(head2))



