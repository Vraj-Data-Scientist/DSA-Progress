class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def search_ele(self, head, ele):
        temp = head
        while(temp):
            if (temp.data == ele):
                return True
            temp = temp.next
        return False

node1 = Node(12)
node2 = Node(22)
node3 = Node(10)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
# node4.next = None (by default)

print(Solution().search_ele(node1, 1))
print(Solution().search_ele(node1, 10))