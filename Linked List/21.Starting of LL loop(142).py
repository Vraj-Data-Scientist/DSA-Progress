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

    def starting_of_loop_ll_brute(self, head: [ListNode]) -> [ListNode]:
        dict1 = {}
        temp = head
        while (temp != None):
            if (temp in dict1):
                return temp
            dict1[temp] = 1
            temp = temp.next
        return None

    def starting_of_loop_ll_optimal(self, head: [ListNode]) -> [ListNode]:
        slow = head
        fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                slow = head
                while (slow != fast):
                    fast = fast.next
                    slow = slow.next
                return slow
        return None


temp = Solution().starting_of_loop_ll_brute(node1)
print(temp.val)
temp = Solution().starting_of_loop_ll_optimal(node1)
print(temp.val)

