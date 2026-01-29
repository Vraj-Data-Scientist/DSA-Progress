class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back

class Solution:
    def arr_to_DLL(self, arr):
        n = len(arr)
        head = Node(arr[0])
        prev = head
        for i in range(1, n):
            temp = Node(arr[i], None, prev)
            prev.next = temp
            prev = temp
        return head

    def traversal(self, head):
        temp = head
        while (temp != None):
            print(temp.data)
            temp = temp.next

    def find_pair_with_sum_k_brute(self, head, k):
        list1 = []
        temp1 = head
        while (temp1 != None):
            temp2 = temp1.next
            while (temp2 != None and (temp1.data + temp2.data) <= k):
                if ((temp1.data + temp2.data) == k):
                    list1.append((temp1.data, temp2.data))
                temp2 = temp2.next
            temp1 = temp1.next
        return list1

    def find_tail(self,head):
        temp = head
        while (temp.next != None):
            temp = temp.next
        return temp

    def find_pair_with_sum_k_optimal(self, head, k):
        list1 = []
        left = head
        right = Solution().find_tail(head)
        while (left.data < right.data):
            if (left.data + right.data == k):
                list1.append((left.data, right.data))
                left = left.next
                right = right.back
            elif (left.data + right.data < k):
                left = left.next
            else:
                right = right.back
        return list1

head1 = Solution().arr_to_DLL([1,2,3,4,9])
print(Solution().find_pair_with_sum_k_brute(head1, 5))
head1 = Solution().arr_to_DLL([1,2,3,4,9])
print(Solution().find_pair_with_sum_k_optimal(head1, 5))


