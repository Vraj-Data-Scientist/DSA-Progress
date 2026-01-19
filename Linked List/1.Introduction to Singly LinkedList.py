class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(12)
node2 = Node(22)
node3 = Node(10)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
# node4.next = None (by default)

class Solution:
    def arr_to_LL(self, arr):
        n = len(arr)
        head = Node(arr[0])
        mover = head
        for i in range(1, n):
            temp = Node(arr[i])
            mover.next = temp
            mover = temp
        return head.next, head.next.next.next, head.next.next.next.next

print(Solution().arr_to_LL([3,2,5,6]))





