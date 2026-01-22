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

    def oddEvenList_brute_1(self, head: [ListNode]) -> [ListNode]:
        if (head == None or head.next == None):
            return head
        list1 = []
        t1 = head
        while (t1 != None and t1.next != None):
            list1.append(t1.val)
            t1 = t1.next.next
        if (t1):
            list1.append(t1.val)
        t2 = head.next
        while (t2 != None and t2.next != None):
            list1.append(t2.val)
            t2 = t2.next.next
        if (t2):
            list1.append(t2.val)
        i = 0
        temp = head
        while (temp != None):
            temp.val = list1[i]
            i += 1
            temp = temp.next
        return head

    def oddEvenList_brute_2(self, head: [ListNode]) -> [ListNode]:
        if (head == None or head.next == None):
            return head
        dummy_head = ListNode(-1)
        curr = dummy_head
        t1 = head
        while (t1 != None and t1.next != None):
            new = ListNode(t1.val)
            curr.next = new
            curr = curr.next
            t1 = t1.next.next
        if (t1):
            new = ListNode(t1.val)
            curr.next = new
            curr = curr.next
        t2 = head.next
        while (t2 != None and t2.next != None):
            new = ListNode(t2.val)
            curr.next = new
            curr = curr.next
            t2 = t2.next.next
        if (t2):
            new = ListNode(t2.val)
            curr.next = new
            curr = curr.next
        temp = head
        t = dummy_head.next
        while (temp != None):
            temp.val = t.val
            temp = temp.next
            t = t.next
        return head

    def oddEvenList_optimal(self, head: [ListNode]) -> [ListNode]:
        if (head == None or head.next == None):
            return head
        odd = head
        even = head.next
        even_head = head.next
        while (even != None and even.next != None):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head

head1 = Solution().arr_to_LL([2,1,3,5,6,4,7])
head2 = Solution().oddEvenList_brute_1(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().oddEvenList_brute_1(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([2,1,3,5,6,4,7])
head2 = Solution().oddEvenList_brute_2(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().oddEvenList_brute_2(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([2,1,3,5,6,4,7])
head2 = Solution().oddEvenList_optimal(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,2,3,4,5])
head2 = Solution().oddEvenList_optimal(head1)
print(Solution().traversal(head2))



