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

    def reverse_ll(self, head: [ListNode]) -> [ListNode]:
        prev = None
        temp = head
        while (temp != None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def isPalindrome_brute_1(self, head:[ListNode]) -> bool:
        len = 0
        temp = head
        while (temp != None):
            len += 1
            temp = temp.next
        temp = head
        stack = []
        i = 1
        while (i <= (len//2)):
            stack.append(temp.val)
            i += 1
            temp = temp.next
        if (len % 2 != 0):
            temp = temp.next
        while (temp != None):
            if (temp.val != stack[-1]):
                return False
            stack.pop()
            temp = temp.next
        return True

    def isPalindrome_brute_2(self, head:[ListNode]) -> bool:
        temp = head
        stack = []
        while (temp != None):
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while (temp != None):
            if (temp.val != stack[-1]):
                return False
            temp = temp.next
            stack.pop()
        return True

    def isPalindrome_optimal(self, head:[ListNode]) -> bool:
        if (head == None or head.next == None):
            return True
        slow = head
        fast = head
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        new_head = Solution().reverse_ll(slow.next)
        first = head
        second = new_head
        while (second != None):
            if (first.val != second.val):
                Solution().reverse_ll(new_head)
                return False
            first = first.next
            second = second.next
        Solution().reverse_ll(new_head)
        return True




head1 = Solution().arr_to_LL([1,2,1,2,1,2,1])
print(Solution().isPalindrome_brute_1(head1))
head1 = Solution().arr_to_LL([1,2,1,1,2])
print(Solution().isPalindrome_brute_1(head1))
head1 = Solution().arr_to_LL([1,2,1,2,1,2,1])
print(Solution().isPalindrome_brute_2(head1))
head1 = Solution().arr_to_LL([1,2,1,1,2])
print(Solution().isPalindrome_brute_2(head1))
head1 = Solution().arr_to_LL([1,2,1,2,1,2,1])
print(Solution().isPalindrome_optimal(head1))
head1 = Solution().arr_to_LL([1,2,1,1,2])
print(Solution().isPalindrome_optimal(head1))
