class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

head = ListNode(5)
head.child = ListNode(6)

head.next = ListNode(10)
head.next.child = ListNode(12)

head.next.next = ListNode(13)
head.next.next.child = ListNode(20)
head.next.next.child.child = ListNode(22)

head.next.next.next = ListNode(7)
head.next.next.next.child = ListNode(17)

class Solution:
    def arr_to_LL(self, arr):
        n = len(arr)
        if (n == 0):
            return None
        head = ListNode(arr[0])
        mover = head
        for i in range(1, n):
            temp = ListNode(arr[i])
            mover.child = temp
            mover = temp
        return head

    def traversal(self, head):
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.child

    def flattenLinkedList_brute(self, head):
        list1 = []
        temp = head
        while (temp != None):
            t2 = temp
            while (t2 != None):
                list1.append(t2.val)
                t2 = t2.child
            temp = temp.next
        list1.sort()
        head = Solution().arr_to_LL(list1)
        return head

    def merge_two_sorted_ll(self, head1, head2):
        t1 = head1
        t2 = head2
        dummy_head = ListNode(-1)
        temp = dummy_head
        while (t1 != None and t2 != None):
            if (t1.val < t2.val):
                temp.child = t1
                temp = t1
                t1 = t1.child
            else:
                temp.child = t2
                temp = t2
                t2 = t2.child
            temp.next = None
        if (t1):
            temp.child = t1
        else:
            temp.child = t2
        result = dummy_head.child
        while result:
            result.next = None
            result = result.child
        return dummy_head.child

    def flattenLinkedList_optimal(self, head):
        if (head == None or head.next == None):
            return head
        merged_head = Solution().flattenLinkedList_optimal(head.next)
        return Solution().merge_two_sorted_ll(head, merged_head)

head2 = Solution().flattenLinkedList_brute(head)
print(Solution().traversal(head2))
head2 = Solution().flattenLinkedList_optimal(head)
print(Solution().traversal(head2))