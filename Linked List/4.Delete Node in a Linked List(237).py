class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(12)
node2 = Node(22)
node3 = Node(10)
node4 = Node(9)
node5 = Node(25)
node6 = Node(30)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
# node6.next = None (by default)

class Solution:
    def traversal(self, head):
        temp = head
        while(temp):
            print(temp.data)
            temp = temp.next

    def delete_first(self, head):
        if (head == None):
            return head
        temp = head
        head = head.next
        temp = None
        return head

    def delete_last(self, head):
        if (head == None or head.next == None):
            return None
        temp = head
        while (temp.next.next is not None):
            temp = temp.next
        temp.next = None
        return head

    def kth_position(self, head, k):
        if (head == None):
            return None
        if (k == 1):
            temp = head
            head = head.next
            temp = None
            return head
        cnt = 0
        temp = head
        prev = None
        while(temp != None):
            cnt += 1
            if (cnt == k):
                prev.next = prev.next.next
                temp = None
                break
            prev = temp
            temp = temp.next
        return head

    def del_val(self, head, val):
        if (head == None):
            return None
        if (head.data == val):
            temp = head
            head = head.next
            temp = None
            return head
        temp = head
        prev = None
        while(temp != None):
            if (temp.data == val):
                prev.next = prev.next.next
                temp = None
                break
            prev = temp
            temp = temp.next
        return head

    def deleteNode_without_head(self, node):
        node.data = node.next.data
        node.next = node.next.next

print(Solution().traversal(node1))
Solution().deleteNode_without_head(node4)
print(Solution().traversal(node1))
Solution().kth_position(node1, 3)
print(Solution().traversal(node1))
Solution().del_val(node2, 25)
print(Solution().traversal(node1))

print(Solution().traversal(Solution().delete_first(node1)))
print(Solution().traversal(Solution().delete_last(node2)))


