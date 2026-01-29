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

    def delete_ele_all_occurances(self, head, key):
        temp = head
        while (temp != None):
            if (temp.data == key):
                if (temp == head):
                    head = head.next
                front = temp.next
                prev = temp.back
                if (front):
                    front.back = prev
                if (prev):
                    prev.next = front
                temp = None
                temp = front
            else:
                temp = temp.next
        return head

head1 = Solution().arr_to_DLL([10,1,10,2,10,3,4,5,10,6,10])
head2 = Solution().delete_ele_all_occurances(head1, 10)
print(Solution().traversal(head2))
