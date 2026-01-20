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
    def traversal(self, head):
        temp = head
        while(temp):
            print(temp.data)
            temp = temp.next

    def insert_first(self, head, val):
        temp = Node(val, head)
        head = temp
        return head

    def insert_last(self, head, val):
        if (head == None):
            return None
        temp = head
        while (temp.next != None):
            temp = temp.next
        temp.next = Node(val)
        return head

    def insert_kth_position(self, head, val, k):
        if (head == None):
            if (k == 1):
                return Node(val)
            else:
                return None
        if (k == 1):
            temp = Node(val, head)
            return temp
        cnt = 0
        temp = head
        while (temp != None):
            cnt += 1
            if (cnt == k-1):
                new = Node(val, temp.next)
                temp.next = new
                return head
            temp = temp.next
        return head

    def insert_before_val_x(self, head, val, new):
        if (head == None):
            return None
        if (head.data == val):
            temp = Node(new, head)
            return temp
        temp = head
        while (temp.next != None):
            if (temp.next.data == val):
                new = Node(new, temp.next)
                temp.next = new
                return head
            temp = temp.next
        return head

print(Solution().traversal(node1))
Solution().insert_kth_position(node1, 3, 3)
print(Solution().traversal(node1))
Solution().insert_last(node1, 30)
print(Solution().traversal(node1))
Solution().insert_before_val_x(node1, 9, 5)
print(Solution().traversal(node1))
Solution().insert_first(node1, 25)
print(Solution().traversal(Solution().insert_first(node1, 25)))