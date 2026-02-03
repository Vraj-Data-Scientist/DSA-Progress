from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

arr = []

node1 = ListNode(1)
node1.next = ListNode(3)
node1.next.next = ListNode(5)
node1.next.next.next = ListNode(7)
arr.append(node1)

node2 = ListNode(2)
node2.next = ListNode(4)
node2.next.next = ListNode(6)
node2.next.next.next = ListNode(8)
arr.append(node2)

node3 = ListNode(0)
node3.next = ListNode(9)
node3.next.next = ListNode(10)
node3.next.next.next = ListNode(11)
arr.append(node3)
print(arr)

class Solution:
    def arr_to_LL(self, arr):
        n = len(arr)
        if (n == 0):
            return None
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

    def mergeKLists_brute(self, lists: List[ListNode]) -> [ListNode]:
        list1 = []
        n = len(lists)
        for i in range(0, n):
            temp = lists[i]
            while (temp != None):
                list1.append(temp.val)
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
                temp.next = t1
                temp = t1
                t1 = t1.next
            else:
                temp.next = t2
                temp = t2
                t2 = t2.next
        if (t1):
            temp.next = t1
        else:
            temp.next = t2
        return dummy_head.next

    def mergeKLists_better_1(self, lists: List[ListNode]) -> [ListNode]:
        n = len(lists)
        if (n == 0):
            return None
        if (n == 1):
            return lists[0]
        head = lists[0]
        for i in range(1, n):
            head = Solution().merge_two_sorted_ll(head, lists[i])
        return head

    def mergeKLists_better_2(self, lists: List[ListNode]) -> [ListNode]:
        n = len(lists)
        if not lists:
            return None
        if  n == 1:
            return lists[0]
        return self.merge_two_sorted_ll(
            lists[0],
            self.mergeKLists_better_2(lists[1:])
        )

    def mergeKLists_optimal(self, lists: List[ListNode]) -> [ListNode]:
        n = len(lists)
        min_heap = []
        counter = 0
        for i in range(0, n):
            if (lists[i] != None):
                heapq.heappush(min_heap, (lists[i].val, counter, lists[i]))
                counter += 1
        d_node = ListNode(-1)
        temp = d_node
        while (min_heap):
            value, cnt, smallest_node = heapq.heappop(min_heap)
            temp.next = smallest_node
            temp = temp.next
            if smallest_node.next:
                counter += 1
                heapq.heappush(min_heap, (smallest_node.next.val, counter, smallest_node.next))
        return d_node.next





# head2 = Solution().mergeKLists_brute(arr)
# print(Solution().traversal(head2))
# head2 = Solution().mergeKLists_better_1(arr)
# print(Solution().traversal(head2))
# head2 = Solution().mergeKLists_better_2(arr)
# print(Solution().traversal(head2))
head2 = Solution().mergeKLists_optimal(arr)
print(Solution().traversal(head2))



