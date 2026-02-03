class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

head = Node(7)
head.next = Node(14)
head.next.next = Node(21)
head.next.next.next = Node(28)

head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next
head.next.next.next.random = head.next

class Solution:
    def traversal_by_next(self, head):
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.next

    def traversal_by_random(self, head):
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.random

    def copyRandomList_brute(self, head: [Node]) -> [Node]:
        if (head == None):
            return head
        dict1 = {}
        temp = head
        while (temp != None):
            copy_node = Node(temp.val)
            dict1[temp] = copy_node
            temp = temp.next
        temp = head
        while (temp != None):
            copy_node = dict1[temp]
            copy_node.next = dict1[temp.next] if temp.next else None
            copy_node.random = dict1[temp.random] if temp.random else None
            temp = temp.next
        return dict1[head]

    def copyRandomList_optimal(self, head: [Node]) -> [Node]:
        if (head == None):
            return head
        temp = head
        while (temp != None):
            copy_node = Node(temp.val)
            copy_node.next = temp.next
            temp.next = copy_node
            temp = temp.next.next
        temp = head
        while (temp != None):
            copy_node = temp.next
            copy_node.random = temp.random.next if temp.random else None
            temp = temp.next.next
        d_node = Node(-1)
        res = d_node
        temp = head
        while (temp != None):
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next
        return d_node.next

head2 = Solution().copyRandomList_brute(head)
print(Solution().traversal_by_next(head2))
print(head2.random.val)
print(head2.next.random.val)
print(head2.next.next.random.val)
print(head2.next.next.next.random.val)
print('=====')
head2 = Solution().copyRandomList_optimal(head)
print(Solution().traversal_by_next(head2))
print(head2.random.val)
print(head2.next.random.val)
print(head2.next.next.random.val)
print(head2.next.next.next.random.val)


