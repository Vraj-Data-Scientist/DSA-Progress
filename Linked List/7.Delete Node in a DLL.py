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

    def delete_first(self, head):
        temp = head
        head = head.next
        head.back = None
        temp.next = None
        temp = None
        return head

    def delete_last(self, head):
        temp = head
        while (temp.next != None):
            temp = temp.next
        prev = temp.back
        prev.next = None
        temp.back = None
        temp = None
        return head

    def delete_kth_position(self, head, k):
        cnt = 0
        temp = head
        while (temp != None):
            cnt += 1
            if (cnt == k):
                break
            temp = temp.next
        prev = temp.back
        front = temp.next
        if (prev == None and front == None):
            return None
        elif (prev == None):
            return Solution().delete_first(head)
        elif (front == None):
            return Solution().delete_last(head)
        else:
            prev.next = front
            front.back = prev
            temp.next = None
            temp.back = None
            temp = None
            return head

    def delete_given_node(self, head, node):
        prev = node.back
        front = node.next
        prev.next = front
        front.back = prev
        node.next = None
        node.back = None
        node = None

head1 = Solution().arr_to_DLL([1,3,5,7,2,4])
print(Solution().traversal(head1))
head3 = Solution().delete_last(head1)
print(Solution().traversal(head3))
head2 = Solution().delete_first(head1)
print(Solution().traversal(head2))
head4 = Solution().delete_kth_position(head2, 3)
print(Solution().traversal(head4))
head5 = Solution().delete_kth_position(head4, 1)
print(Solution().traversal(head5))
head6 = Solution().delete_kth_position(head5, 2)
print(Solution().traversal(head6))
head7 = Solution().delete_kth_position(head6, 1)
print(Solution().traversal(head7))
head8 = Solution().arr_to_DLL([1,3,5,7,2,4])
print(Solution().traversal(head8))
Solution().delete_given_node(head8, head8.next.next.next)
print(Solution().traversal(head8))

