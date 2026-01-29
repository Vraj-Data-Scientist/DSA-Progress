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

arr = [2,3,1,6,9,5,0]
merge_sort(arr, 0, len(arr)-1)
print(arr)

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

    def merge_two_sorted_ll_brute(self, head1, head2):
        t1 = head1
        t2 = head2
        list1 = []
        while (t1 != None):
            list1.append(t1.val)
            t1 = t1.next
        while (t2 != None):
            list1.append(t2.val)
            t2 = t2.next
        n = len(list1)
        merge_sort(list1, 0, n-1)
        head = Solution().arr_to_LL(list1)
        return head

    def merge_two_sorted_ll_optimal(self, head1, head2):
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

head1 = Solution().arr_to_LL([2,4,8,10])
head2 = Solution().arr_to_LL([1,3,3,6,11,14])
head3 = Solution().merge_two_sorted_ll_brute(head1, head2)
print(Solution().traversal(head3))
head3 = Solution().merge_two_sorted_ll_optimal(head1, head2)
print(Solution().traversal(head3))


