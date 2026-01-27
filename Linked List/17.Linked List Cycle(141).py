class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(12)
node2 = ListNode(22)
node3 = ListNode(10)
node4 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

class Solution:
    def traversal(self, head):
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.next

    def hasCycle_brute(self, head: [ListNode]) -> bool:
        dict1 = {}
        temp = head
        while (temp != None):
            if (temp in dict1):
                return True
            dict1[temp] = 1
            temp = temp.next
        return False

    def hasCycle_optimal(self, head: [ListNode]) -> bool:
        slow = head
        fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False

print(Solution().hasCycle_brute(node1))
print(Solution().hasCycle_optimal(node1))

