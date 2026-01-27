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
node4.next = node3

class Solution:
    def traversal(self, head):
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.next

    def len_Cycle_brute(self, head: [ListNode]) -> bool:
        dict1 = {}
        temp = head
        timer = 1
        while (temp != None):
            if (temp in dict1):
                return (timer - dict1[temp])
            dict1[temp] = timer
            timer += 1
            temp = temp.next
        return 0

    def find_len_loop(self, slow: [ListNode], fast: [ListNode]) -> int:
        cnt = 1
        slow = slow.next
        while(fast != slow):
            slow = slow.next
            cnt += 1
        return cnt

    def len_Cycle_optimal(self, head: [ListNode]) -> bool:
        slow = head
        fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return Solution().find_len_loop(slow, fast)
        return 0

print(Solution().len_Cycle_brute(node1))
print(Solution().len_Cycle_optimal(node1))