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

    def rearrange_brute(self, head):
        cnt_0 = 0
        cnt_1 = 0
        cnt_2 = 0
        temp = head
        while (temp != None):
            if (temp.val == 0):
                cnt_0 += 1
            elif (temp.val == 1):
                cnt_1 += 1
            else :
                cnt_2 += 1
            temp = temp.next
        temp = head
        while (temp != None):
            if (cnt_0):
                temp.val = 0
                cnt_0 -= 1
            elif (cnt_1):
                temp.val = 1
                cnt_1 -= 1
            else:
                temp.val = 2
                cnt_2 -= 1
            temp = temp.next
        return head

    def rearrange_optimal(self, head):
        zero_head = ListNode(-1)
        one_head = ListNode(-1)
        two_head = ListNode(-1)
        zero = zero_head
        one = one_head
        two = two_head
        temp = head
        while (temp != None):
            if (temp.val == 0):
                zero.next = temp
                zero = temp
            elif (temp.val == 1):
                one.next = temp
                one = temp
            else:
                two.next = temp
                two = temp
            temp = temp.next
        zero.next = one_head.next if one_head.next else two_head.next
        one.next = two_head.next
        two.next = None
        head = zero_head.next
        return head





head1 = Solution().arr_to_LL([1,0,1,2,0,2,1])
head2 = Solution().rearrange_brute(head1)
print(Solution().traversal(head2))
head1 = Solution().arr_to_LL([1,0,1,2,0,2,1])
head2 = Solution().rearrange_optimal(head1)
print(Solution().traversal(head2))