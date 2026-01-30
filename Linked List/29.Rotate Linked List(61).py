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

    def find_nth_node(self, head, n):
        temp = head
        cnt = 1
        while (temp != None):
            if (cnt == n):
                return temp
            cnt += 1
            temp = temp.next
        return temp

    def rotateRight(self, head:[ListNode], k: int) -> [ListNode]:
        if (head == None or head.next == None):
            return head
        tail = head
        len = 1
        while (tail.next != None):
            tail = tail.next
            len += 1
        if (k % len == 0):
            return head
        k = k % len
        tail.next = head
        new_last = Solution().find_nth_node(head, len - k)
        head = new_last.next
        new_last.next = None
        return head

head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().rotateRight(head1, 3)
print(Solution().traversal(head2))