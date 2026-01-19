class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def traversal(self, head):
        temp = head
        while(temp):
            print(temp.data)
            temp = temp.next

    def length(self, head):
        temp = head
        cnt = 0
        while(temp):
            cnt += 1
            temp = temp.next
        return cnt

if __name__ == "__main__":
    node1 = Node(12)
    node2 = Node(22)
    node3 = Node(10)
    node4 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    # node4.next = None (by default)

    print(Solution().traversal(node1))
    print(Solution().length(node1))