from typing import List

def merge_sort(arr:List[int], low:int, high:int):
    if (low >= high):
        return None
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

def merge(arr:List[int], low:int, mid:int, high:int):
    left = low
    right = mid + 1
    temp = []
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while (left <= mid):
        temp.append(arr[left])
        left += 1
    while (right <= high):
        temp.append(arr[right])
        right += 1
    for i in range(low, high+1):
        arr[i] = temp[i - low]

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

    def sort_ll_brute(self, head):
        list1 = []
        temp = head
        while (temp != None):
            list1.append(temp.val)
            temp = temp.next
        merge_sort(list1, 0, len(list1)-1)
        i = 0
        temp = head
        while (temp != None):
            temp.val = list1[i]
            i += 1
            temp = temp.next
        return head

    def middleNode(self, head: [ListNode]) -> [ListNode]:
        slow = head
        fast = head.next
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

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

    def merge_sort_ll(self, head):
        if (head == None or head.next == None):
            return head
        mid = Solution().middleNode(head)
        left_head = head
        right_head = mid.next
        mid.next = None
        left_head = Solution().merge_sort_ll(left_head)
        right_head = Solution().merge_sort_ll(right_head)
        return Solution().merge_two_sorted_ll(left_head, right_head)

head1 = Solution().arr_to_LL([3,4,2,1,5,0])
head2 = Solution().sort_ll_brute(head1)
print(Solution().traversal(head2))
head2 = Solution().merge_sort_ll(head1)
print(Solution().traversal(head2))