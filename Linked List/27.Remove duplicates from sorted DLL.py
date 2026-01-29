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

    def remove_duplicates_from_sorted_ll(self,head):
        temp = head
        while (temp != None):
            front = temp.next
            while (front != None and temp.data == front.data):
                duplicate = front
                front = front.next
                duplicate = None
            temp.next = front
            if (front):
                front.back = temp
            temp = temp.next
        return head

head1 = Solution().arr_to_DLL([1,1,1,2,3,3,4,4])
head2 = Solution().remove_duplicates_from_sorted_ll(head1)
print(Solution().traversal(head2))
