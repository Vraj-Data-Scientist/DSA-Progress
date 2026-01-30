class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def arr_to_LL(self, arr):
        n = len(arr)
        head = ListNode(arr[0])
        mover = head
        for i in range(1, n):
            temp = ListNode(arr[i])
            mover.next = temp
            mover = temp
        return head

    def traversal(self, head):
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.next

    def reverse(self, head: [ListNode]) -> [ListNode]:
        prev = None
        temp = head
        while (temp != None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def find_kth_node(self, temp, k):
        k -= 1
        while (temp != None and k > 0):
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:
        temp = head
        while (temp != None):
            kth_node = Solution().find_kth_node(temp, k)
            if (kth_node == None):
                if (prev_group_last):
                    prev_group_last.next = temp
                break
            next_group_first = kth_node.next
            kth_node.next = None
            Solution().reverse(temp)
            if (temp == head):
                head = kth_node
            else:
                prev_group_last.next = kth_node
            prev_group_last = temp
            temp = next_group_first
        return head

head1 = Solution().arr_to_LL([1,2,3,4,5,6,7,8,9,0])
head2 = Solution().reverseKGroup(head1, 3)
print(Solution().traversal(head2))
