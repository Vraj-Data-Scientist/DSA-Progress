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

Solution().arr_to_DLL([1,2,3,1.5])
print(Solution().traversal(Solution().arr_to_DLL([1,2,3,1.5])))
