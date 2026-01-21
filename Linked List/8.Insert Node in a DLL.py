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

    def insert_before_first(self, head, val):
        new = Node(val, head, None)
        head.back = new
        return new

    def insert_before_last(self, head, val):
        temp = head
        while (temp.next != None):
            temp = temp.next
        prev = temp.back
        new = Node(val, temp, prev)
        prev.next = new
        temp.back = new
        return head

    def insert_at_kth_position(self, head, val, k):
        cnt = 0
        temp = head
        while (temp != None):
            cnt += 1
            if (cnt == k):
                break
            temp = temp.next
        prev = temp.back
        new = Node(val, temp, prev)
        prev.next = new
        temp.back = new
        return head

    def insert_before_given_node(self, head, val, node):
        prev = node.back
        new = Node(val, node, prev)
        prev.next = new
        node.back = new
        return head

head1 = Solution().arr_to_DLL([1,5,7,2])
head2 = Solution().insert_before_first(head1, 10)
print(Solution().traversal(head2))
head1 = Solution().arr_to_DLL([1,5,7,2])
head2 = Solution().insert_before_last(head1, 10)
print(Solution().traversal(head2))
head1 = Solution().arr_to_DLL([1,5,7,2])
head2 = Solution().insert_at_kth_position(head1, 10, 3)
print(Solution().traversal(head2))
head1 = Solution().arr_to_DLL([1,5,7,2])
head2 = Solution().insert_before_given_node(head1, 10, head1.next)
print(Solution().traversal(head2))



