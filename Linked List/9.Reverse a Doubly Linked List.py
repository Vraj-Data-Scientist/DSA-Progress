class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back

class Solution:
    def arr_to_DLL(self, arr):
        n = len(arr)
        head = Node(arr[0])
        prev = head
        for i in range(1, n):
            temp = Node(arr[i], None, prev)
            prev.next = temp
            prev = temp
        return head

    def traversal(self, head):
        temp = head
        while (temp != None):
            print(temp.data)
            temp = temp.next

    def reverse_DLL_brute(self, head):
        stack = []
        temp = head
        while (temp != None):
            stack.append(temp.data)
            temp = temp.next
        temp = head
        while (temp != None):
            temp.data = stack[-1]
            stack.pop()
            temp = temp.next
        return head

    def reverse_DLL_optimal(self, head):
        temp = head
        while (temp != None):
            last = temp.back
            temp.back = temp.next
            temp.next = last
            temp = temp.back
        return last.back

head1 = Solution().arr_to_DLL([1,5,7,2])
head2 = Solution().reverse_DLL_brute(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_DLL([1,5,7,2])
head2 = Solution().reverse_DLL_optimal(head1)
print(Solution().traversal(head2))
